import factory
from products.models import Category, Product

class CategoryFactory(factory.django.DjangoModelFactory):
    name = "jojo"
    slug = "jojo"
    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    description = factory.Faker('text')
    price = None
    image = '/home/zeus/Imagens/tesla_car_PNG46.png'
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Product
        
