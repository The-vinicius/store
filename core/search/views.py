from django.shortcuts import render
from django.views.generic.list import ListView
from products.models import Product
from django.db.models import Q
from products.utils import FilterPrice


class SearchProductView(ListView):
    template_name = 'search/search.html'
    paginate_by = 20


    def get_queryset(self, *args, **kwargs):
        global price

        query = self.request.GET.get('q', None)
        queryset = Product.search.q(query)

        price = FilterPrice(queryset)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        context['price'] = price
        return context
