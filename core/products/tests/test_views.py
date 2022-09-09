from pytest import mark
from pytest import fixture
from django.urls import reverse
from ..models import Category, Product

@fixture
def category():
    return Category.objects.create(name='clock')

@mark.django_db
def test_category_views_status_code_200(client):
    url = reverse('category')
    response = client.get(url)
    assert response.status_code == 200


@mark.django_db
def test_category_list_views_status_code_200(client, category):
    # gera url para category_list com objeto category
    url = reverse('category_list', kwargs={'slug': category.slug})
    response = client.get(url)
    assert response.status_code == 200


@mark.django_db
def test_product_detail_view_status_code_200(client, category):
    # create product
    product = Product.objects.create(
        name='besta',
        description='qualquer coisa?',
        price=12345,
        category=category,
        image='/home/zeus/Imagens/tesla_car_PNG46.png',
       )
    # gera url para detail com objeto product
    url = reverse('products:detail', kwargs={'slug': product.slug})
    response = client.get(url)
    assert response.status_code == 200
