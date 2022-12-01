from pytest import mark
from django.urls import reverse


@mark.django_db
def test_searchview(client, price, product_multiplus):
    url = reverse("search:query")

    data = {
        'q': product_multiplus[0].name,
    }
    response = client.get(url, data)

    assert response.context['object_list'].count() == 1
