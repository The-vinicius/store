from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic.edit import FormView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Category, Product, ImageProduct
from .forms import ProductForm, ImageForm, ImageProductFormset
from django.urls import reverse_lazy
from django.db.models import Max
from .utils import FilterPrice


class ProductFormView(FormView):
    template_name = 'products/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('category')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('image') # get images

        if form.is_valid():
            # get product
            product = form.save()
            # for list of images
            for f in files:
                # create images relationships product
                ImageProduct.objects.create(product=product, photo=f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ListProductView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 20

    def get_queryset(self):
        queryset = Product.available.all()

        return queryset


class CategoryProductView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 20

    def get_queryset(self):
        # var global get_context_data
        global category_slug
        global price

        queryset = Product.available.all()
        category_slug = self.kwargs.get('slug')

        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)

        # get filter price
        price = FilterPrice(queryset)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['price'] = price
        context['slug'] = category_slug
        return context


class ProductDetailView(DetailView):
    model = Product


def edit_product(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None, instance=product)
        formset = ImageProductFormset(request.POST or None, request.FILES or None, instance=product)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('products:detail', slug=product.slug)
    else:
        form = ProductForm(instance=product)
        formset = ImageProductFormset(instance=product)

    context = {
        'form': form,
        'product': product,
        'formset': formset
    }

    return render(request, 'products/edit_product.html', context)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('category')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
