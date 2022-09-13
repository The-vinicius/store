from ..models import Category
from pytest import fixture


@fixture
def category():
    return Category.objects.create(name='clock')


