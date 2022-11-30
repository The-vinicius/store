from django.shortcuts import render
from django.views.generic.list import ListView
from products.models import Product
from django.db.models import Q


class SearchProductView(ListView):
    template_name = 'search/search.html'


    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('q', None)
        lookups = (
            Q(name__icontains=query)|
            Q(description__icontains=query)
        )
        queryset = Product.objects.filter(lookups)
        return queryset
