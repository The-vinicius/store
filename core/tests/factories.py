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
    image = factory.django.ImageField(color='blue')
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Product
        
