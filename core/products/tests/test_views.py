from pytest import mark
from django.urls import reverse
from ..models import Category

@mark.django_db
def test_category_views_status_code_200(client):
    url = reverse('category')
    response = client.get(url)
    assert response.status_code == 200
