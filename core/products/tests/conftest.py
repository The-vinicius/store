from ..models import Category, Product
from pytest import fixture
from rolepermissions.roles import assign_role

@fixture
def category():
    return Category.objects.create(name='clock')

@fixture
def product(category):
    product = Product.objects.create(
        name='besta',
        description='qualquer coisa?',
        price=12345,
        category=category,
        image='/home/zeus/Imagens/tesla_car_PNG46.png',
       )
    return product

@fixture
def user(django_user_model):
    user = django_user_model.objects.create(username="someone", password="pass")
    return user

@fixture
def user_gerente(user):
    assign_role(user, 'gerente')
    return user
