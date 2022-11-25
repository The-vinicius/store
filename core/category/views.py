from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from products.models import Category, Product
from products.utils import FilterPrice
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import CategoryForm


class CategoryView(ListView):
    queryset = Category.objects.all()
    paginate_by = 12
    template_name = 'category/category_list.html'


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


class CategoryFormView(FormView):
    template_name = 'category/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:categories')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

