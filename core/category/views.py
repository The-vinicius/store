from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from products.models import Category, Product
from products.utils import FilterPrice


class CategoryView(ListView):
    queryset = Category.objects.all()
    paginate_by = 12
    template_name = 'products/category_list.html'


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

