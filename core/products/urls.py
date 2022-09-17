from django.urls import path
from .views import ProductFormView, ListProductView, ProductDetailView
from rolepermissions.decorators import has_permission_decorator


app_name = 'products'

urlpatterns = [
    path('add-product',
         has_permission_decorator('add_product')(ProductFormView.as_view()), name='add'),
    path('todos/', ListProductView.as_view(), name='list_product'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
]
