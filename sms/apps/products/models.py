import uuid

from autoslug import AutoSlugField
from django.db import models

from sms.apps.accounts.models import TimeStampedModel

# from django_resized import ResizedImageField


# Create your models here.
class Product(models.Model):
    IN_STOCK = 1
    OUT_OF_STOCK = 0
    STATUS_CHOICES = (
        (IN_STOCK, 'In stock'),
        (OUT_OF_STOCK, 'Out of stock')
    )
    LABEL_CHOICES = (
        ('P', 'primary'),
        ('S', 'secondary'),
        ('D', 'danger'),
    )
    status = models.PositiveIntegerField(
        choices=STATUS_CHOICES, default=IN_STOCK
    )
    product_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=200,)
    description = models.TextField(blank=True, null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    sub_category = models.ForeignKey('SubCategory', null=True, blank=True, on_delete=models.CASCADE)
    product_image = models.FileField(upload_to='products', null=True, blank=True)
    product_video = models.FileField(upload_to='products', null=True, blank=True)
    tax = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    shipping_charge = models.FloatField(null=True, blank=True)
    net_amount = models.FloatField(null=True, blank=True)
    offer_percentage = models.IntegerField(null=True, blank=True)
    # category = models.ForeignKey(category)
    
    def __str__(self):
        return self.name


class Category(TimeStampedModel):
    title = models.CharField(max_length=200, blank=True, null=True)
    slug = AutoSlugField(unique=True,)

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class SubCategory(TimeStampedModel):
    title = models.CharField(max_length=200, blank=True, null=True)
    slug = AutoSlugField(unique=True,)

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'sub-category'
        verbose_name_plural = 'sub-categories'

    def __str__(self):
        return self.title
    