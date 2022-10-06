from django.views.generic.list import ListView
from products.models import Product, Category
from django.shortcuts import get_object_or_404


class FilterProductView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 20

    def get_queryset(self):
        queryset = Product.available.all()
        category_slug = self.kwargs.get('slug')
        print(self.kwargs)

        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)

        return queryset

# Create your views here.
