from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Product
from .forms import ProductForm


class CategoryView(ListView):
    queryset = Category.objects.all()
    paginate_by = 12
    template_name = 'products/category_list.html'


class ProductFormView(CreateView):
    template_name = 'products/product_form.html'
    form_class = ProductForm
    model = Product
    success_url = '/produtos/todos/'

class ListProductView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 20

    def get_queryset(self):
        queryset = Product.available.all()

        return queryset
