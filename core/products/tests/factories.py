import factory
from ..models import Category, Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "jojo"

class ProductFactory(factory.django.DjangoModelFactory):
    name= factory.Faker('name')
    description= factory.Faker('text')
    price= None
    image= '/home/zeus/Imagens/tesla_car_PNG46.png'
    category= factory.SubFactory(CategoryFactory)

    class Meta:
        model = Product
        
