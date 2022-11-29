import pytest
from django.urls import reverse
from products.forms import ProductForm
from products.models import Product


@pytest.mark.django_db
def test_post_product_with_permissions_gerente_response_url_categorias(
    category, user_gerente, client
):
    client.force_login(user=user_gerente)
    url = reverse("products:add_product")
    with open('tests/img/test.jpg', 'rb') as img:
        data = {
            "name": 'vini',
            "description": 'vamos ver no que dar',
            "category": category.id,
            "price": 1234,
            "is_available": True,
            "image": img,
        }
        response = client.post(url, data)
    assert response.url == '/categorias/'


@pytest.mark.django_db
def test_url_add_product_no_permissions_gerente_response_status_code_403(client, user):
    client.force_login(user=user)
    url = reverse("products:add_product")
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_url_add_product_no_login_response_status_code_403(client):
    url = reverse("products:add_product")
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_url_add_product_with_permissions_gerente_response_status_code_200(
    client, user_gerente
):
    client.force_login(user=user_gerente)

    url = reverse("products:add_product")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_criar_category_url_categorias(
    user_gerente, client
):
    client.force_login(user=user_gerente)
    url = reverse("category:add_category")
    with open('tests/img/test.jpg', 'rb') as img:
        data = {
            "name": 'vini',
            "image": img,
        }
        response = client.post(url, data)
    assert response.url == '/categorias/'
