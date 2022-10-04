from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
from model_utils.models import TimeStampedModel
from django.db.models.signals import pre_save
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
from decimal import Decimal
from datetime import date

# filtrar todos os produtos que estam disponíveis
class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, populate_from="name")
    image = models.ImageField("category/img", blank=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:list_by_category", kwargs={"slug": self.slug})


class Product(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    slug = AutoSlugField(populate_from="name", unique=False)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="products/img/", blank=True)
    objects = models.Manager()
    available = AvailableManager()
    offer_available = models.BooleanField(default=False)
    offer_price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    rebate = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    offer_time = models.DateField(auto_now=True)
    history = AuditlogHistoryField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})


class ImageProduct(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='products/photo/', blank=True)

    def __str__(self):
        return self.product.name


def pre_save_offer_price(sender, instance, **kwargs):
    if instance.rebate > 0:
        instance.offer_price = Decimal(instance.price) - Decimal(instance.rebate)


pre_save.connect(pre_save_offer_price, sender = Product)

auditlog.register(Product, include_fields=['price', 'offer_price', 'rebate',])
