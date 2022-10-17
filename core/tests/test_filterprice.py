from products.utils import FilterPrice
from pytest import mark
from products.models import Product

@mark.django_db(transaction=True)
def test_filterprice_price1(price):
    assert price.price1() == 30

@mark.django_db(transaction=True)
def test_filterprice_price2(price):
    assert price.price2() == 60

@mark.django_db(transaction=True)
def test_filterprice_bitween_price(price):
    assert price.bitween_price() == True

@mark.django_db(transaction=True)
def test_filterprice_max_price(price):
    assert price.max_price() == 90

@mark.django_db(transaction=True)
def test_filterprice_result_count(price):
    assert price.result_count() == 9
