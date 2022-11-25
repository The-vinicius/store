from django.urls import path
from .views import CategoryView, CategoryProductView, CategoryFormView

app_name = "category"

urlpatterns = [
    path("", CategoryView.as_view(), name="categories"),
    path('list/<slug:slug>/', CategoryProductView.as_view(), name='category_list'),
    path('criar/', CategoryFormView.as_view(), name='add_category'),
]
