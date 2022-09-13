from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Category, Product, ImageProduct
from .forms import ProductForm
from django.urls import reverse_lazy


class CategoryView(ListView):
    queryset = Category.objects.all()
    paginate_by = 12
    template_name = 'products/category_list.html'


class ProductFormView(FormView):
    template_name = 'products/product_form.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('products:list_product')

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
        queryset = Product.available.all()
        category_slug = self.kwargs.get('slug')

        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)

        return queryset


class ProductDetailView(DetailView):
    model = Product

