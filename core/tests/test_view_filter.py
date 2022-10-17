from django.urls import reverse
from pytest import mark


@mark.django_db(transaction=True)
def test_views_fiter_product_view_status_code_200(client, price, category_factory, product_multiplus):
    url = reverse(
        "filter:result",
        kwargs={
            "slug": category_factory.slug,
            "price_gt": price.price1(),
            "price_lt": price.price2(),
        },
    )

    response = client.get(url)

    assert response.status_code == 200
