from django.urls import reverse
from pytest import mark


@mark.django_db
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


@mark.django_db
def test_filter_product_content_sem_resultados(client, category):
    url = reverse(
        "filter:result",
         kwargs={
            "slug": category.slug,
            "price_gt": 100,
            "price_lt": 100,
        },
    )
    response = client.get(url)
    x = b'Nenhum Produto Para Categoria' in response.content
    assert x == True


@mark.django_db
def test_views_fiter_search_product_count_1(client, price, product_multiplus):
    url = reverse(
        "filter:search",
        kwargs={
            "query": product_multiplus[0].name,
            "price_gt": 0,
            "price_lt": product_multiplus[3].price,
        },
    )

    response = client.get(url)

    assert response.context['object_list'].count() == 1
