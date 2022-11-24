import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_delete_product_view(client, product, user_gerente):
    client.force_login(user=user_gerente)
    url = reverse("products:delete", kwargs={'pk': product.pk})
    response = client.post(url)
    assert response.url == '/categorias/' 
