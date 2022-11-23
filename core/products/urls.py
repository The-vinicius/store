from django.urls import path
from .views import ProductFormView, ListProductView, ProductDetailView, edit_product, ProductDeleteView
from rolepermissions.decorators import has_permission_decorator


app_name = "products"

urlpatterns = [
    path(
        "add-product",
        has_permission_decorator("add_product")(ProductFormView.as_view()),
        name="add",
    ),
    path("todos/", ListProductView.as_view(), name="list_product"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("edit/<pk>/", has_permission_decorator("edit_product")(edit_product), name="edit"),
    path("apagar/<int:pk>/", ProductDeleteView.as_view(), name='delete'),
]
