import pytest 
from django.urls import reverse


@pytest.mark.django_db
def test_edit_name_product(client, product, user_gerente, image_product, category):

    client.force_login(user=user_gerente)
    url = reverse("products:edit", kwargs={'pk': product.pk})
    data = {
        "name": 'camisa',
        "description": product.description,
        "category": category.id,
        "price": product.price,
        "is_available": product.is_available,
        # formset validating
        'images-TOTAL_FORMS': '1',
        'images-INITIAL_FORMS': '0',
    }
    response = client.post(url, data)
    response = client.get(response.url)
    assert b'Camisa' in response.content


@pytest.mark.django_db
def test_imageproductformset(client, product, user_gerente, image_product, category):
    client.force_login(user=user_gerente)
    url = reverse("products:edit", kwargs={'pk': product.pk})
    # open image post edit product view
    with open('tests/img/gol.jpg', 'rb') as img:
        data = {
            "name": 'camisa',
            "description": product.description,
            "category": category.id,
            "price": product.price,
            "is_available": product.is_available,
            # formset validating
            "images-0-photo": img,
            'images-TOTAL_FORMS': '1',
            'images-INITIAL_FORMS': '0',
        }
        response = client.post(url, data)
    # get url detail
    response = client.get(response.url)
    # get imageproduct
    image = response.context['product'].images.last()
    assert image.photo.url == '/media/products/photo/gol.jpg'
