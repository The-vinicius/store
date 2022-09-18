import pytest
from django.urls import reverse
from ..forms import ProductForm
from ..models import Product
from rolepermissions.roles import assign_role
from rolepermissions.permissions import grant_permission


@pytest.mark.django_db
def test_post_product_with_permissions_gerente_response_status_code_200(
    category, product, django_user_model, client
):
    user = django_user_model.objects.create(username="someone", password="pass")
    # user permissions of gerente
    assign_role(user, "gerente")
    # force login
    client.force_login(user=user)

    data = {
        "name": product.name,
        "description": product.description,
        "category": product.category,
        "price": product.price,
        "is_available": product.is_available,
        "image": "/home/zeus/kali-linux-wallpaper-hd-69-images.jpg",
    }
    url = reverse("products:add")
    response = client.post(url, data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_url_add_product_no_permissions_gerente_response_status_code_403(client):
    url = reverse("products:add")
    response = client.get(url)
    assert response.status_code == 403
