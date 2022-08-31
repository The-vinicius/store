from django.urls import path
from .views import ProductFormView

app_name = 'product'

urlpatterns = [
    path('add-product', ProductFormView.as_view(), name='add'),
]
