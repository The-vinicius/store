from django.shortcuts import render
from django.views.generic.list import ListView
from products.models import Category

class CategoryView(ListView):
    queryset = Category.objects.all()
    paginate_by = 12
    template_name = 'products/category_list.html'

