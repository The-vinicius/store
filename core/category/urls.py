from django.urls import path
from .views import CategoryView, CategoryProductView, CategoryFormView
from rolepermissions.decorators import has_permission_decorator
from django.views.decorators.cache import cache_page

app_name = "category"

urlpatterns = [
    path("", cache_page(60*15)(CategoryView.as_view()), name="categories"),
    path('list/<slug:slug>/', CategoryProductView.as_view(), name='category_list'),
    path(
        'criar/',
        has_permission_decorator('add_category')(CategoryFormView.as_view()),
        name='add_category'
    ),
]
