from django.views.generic.list import ListView
from products.models import Product, Category
from django.shortcuts import get_object_or_404


class FilterProductView(ListView):
    template_name = "products/products_list.html"
    paginate_by = 20

    def get_queryset(self):
        queryset = Product.available.all()
        category_slug = self.kwargs.get("slug")
        print(self.kwargs)
        # pegando os valores do form        
        gt = self.kwargs.get('price_gt')#great than
        lt = self.kwargs.get('price_lt')#less than

        if not gt:
            gt = 0

        if not lt or int(gt) > int(lt):
            lt = 1000000

        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category, price__gt=gt, price__lt=lt)

        return queryset
