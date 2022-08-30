from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Product


class CategoryView(ListView):
    queryset = Category.objects.all()
    paginate_by = 12
    template_name = 'products/category_list.html'

