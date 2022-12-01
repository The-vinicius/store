from django.views.generic.list import ListView
from products.models import Product, Category
from django.shortcuts import get_object_or_404
from products.utils import FilterPrice
from django.db.models import Max


class FilterProductView(ListView):
    template_name = "products/products_list.html"
    paginate_by = 20

    def get_queryset(self):
        # var global get_context_data
        global price
        global category_slug
        
        queryset = Product.available.all()
        category_slug = self.kwargs.get("slug")

        # pegando os valores do form
        gt = self.kwargs.get("price_gt")  # great than
        lt = self.kwargs.get("price_lt")  # less than

        if not gt:
            gt = 0
        # gt can't lt
        if not lt or int(gt) > int(lt):
            lt = 1000000

        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(
                category=self.category, price__gt=gt, price__lte=lt
            )
        # get filter price
        if queryset.exists():
            price = FilterPrice(queryset)
        else:
            price = 0

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["slug"] = category_slug
        context["price"] = price
        return context


class FilterSearchView(ListView):
    template_name = "search/search.html"
    paginate_by = 20

    def get_queryset(self):
        # var global get_context_data
        global price

        query = self.kwargs.get("query")

        # pegando os valores do form
        gt = self.kwargs.get("price_gt")  # great than
        lt = self.kwargs.get("price_lt")  # less than

        if not gt:
            gt = 0
        # gt can't lt
        if not lt or int(gt) > int(lt):
            lt = 1000000

        queryset = Product.search.q(query)
        queryset = queryset.filter(
            price__gt=gt, price__lte=lt
        )

        # get filter price
        if queryset.exists():
            price = FilterPrice(queryset)
        else:
            price = 0

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.kwargs.get("query")
        context["price"] = price
        return context
