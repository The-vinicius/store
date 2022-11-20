import pytest
from django.urls import reverse
from products.forms import ProductForm
from products.models import Product


@pytest.mark.django_db
def test_post_product_with_permissions_gerente_response_status_code_200(
    category, product, user_gerente, client
):
    client.force_login(user=user_gerente)
    url = reverse("products:add")
    with open('tests/img/test.jpg', 'rb') as img:
        data = {
            "name": product.name,
            "description": product.description,
            "category": 1,
            "price": product.price,
            "is_available": product.is_available,
            "image": img,
        }
        response = client.post(url, data)
    assert response.url == '/categorias/'


@pytest.mark.django_db
def test_url_add_product_no_permissions_gerente_response_status_code_403(client, user):
    client.force_login(user=user)
    url = reverse("products:add")
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_url_add_product_no_login_response_status_code_403(client):
    url = reverse("products:add")
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_url_add_product_with_permissions_gerente_response_status_code_200(
    client, user_gerente
):
    client.force_login(user=user_gerente)

    url = reverse("products:add")
    response = client.get(url)
    assert response.status_code == 200
