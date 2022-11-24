from django.urls import path
from .views import CategoryView, CategoryProductView

app_name = "category"

urlpatterns = [
    path("", CategoryView.as_view(), name="categories"),
    path('<slug:slug>/', CategoryProductView.as_view(), name='category_list'),
]
