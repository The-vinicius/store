from ..models import Category, Product
from pytest import fixture
from rolepermissions.roles import assign_role
from .factories import ProductFactory
from ..utils import FilterPrice


@fixture
def category():
    return Category.objects.create(name="clock")


@fixture
def product(category):
    product = Product.objects.create(
        name="besta",
        description="qualquer coisa?",
        price=12345,
        category=category,
        image="/home/zeus/Imagens/tesla_car_PNG46.png",
    )
    return product


@fixture
def user(django_user_model):
    user = django_user_model.objects.create(username="someone", password="pass")
    return user


@fixture
def user_gerente(user):
    assign_role(user, "gerente")
    return user


@fixture
def product_multiplus(db):
    return ProductFactory.build_batch(9)

"""
save products in db, by query filter
producsts price, param class FilterPrice
only query products.
"""
@fixture
def query_product(product_multiplus):
    # save category in db
    prices = list(range(10,100,10))
    product_multiplus[0].category.save()
    for i, product in enumerate(product_multiplus):
        # get category and save product
        product.category = Category.objects.first()
        product.price = prices[i]
        product.save()
    return Product.objects.all()


@fixture
def price(query_product):
    return FilterPrice(query_product)
