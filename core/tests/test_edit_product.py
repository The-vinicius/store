import pytest 
from django.urls import reverse


@pytest.mark.django_db
def test_edit_name_product(client, product, user_gerente):

    client.force_login(user=user_gerente)
    url = reverse("products:edit", kwargs={'pk': product.pk})
    data = {
        "name": 'camisa',
    }
    response = client.post(url, data)
    assert response.context['product'].name == 'camisa'

