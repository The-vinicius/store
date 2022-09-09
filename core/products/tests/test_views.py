from pytest import mark
from django.urls import reverse
from ..models import Category

@mark.django_db
def test_category_views_status_code_200(client):
    url = reverse('category')
    response = client.get(url)
    assert response.status_code == 200


@mark.django_db
def test_category_list_views_status_code_200(client):
    # create category
    category = Category.objects.create(name='clock')
    # gera url para category_list com objeto category
    url = reverse('category_list', kwargs={'slug': category.slug})
    response = client.get(url)
    assert response.status_code == 200
