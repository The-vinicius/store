from django.urls import path
from .views import ProductFormView, ListProductView

app_name = 'products'

urlpatterns = [
    path('add-product', ProductFormView.as_view(), name='add'),
    path('todos/', ListProductView.as_view(), name='list_product'),
]
