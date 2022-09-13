import pytest
from django.urls import reverse
from ..forms import ProductForm
from ..models import Product

@pytest.mark.django_db
def test_product_form_is_valid(client, category, product):
    data = {'name': product.name,
            'description': product.description,
            'category': product.category,
            'price': product.price,
            'is_available': product.is_available,
            'image': '/home/zeus/kali-linux-wallpaper-hd-69-images.jpg',
           }
    url = reverse('products:add')
    response = client.post(url, data)
    assert response.status_code == 200
