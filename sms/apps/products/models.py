import uuid

from django.db import models


# Create your models here.
class Product(models.Model):
    IN_STOCK = 1
    OUT_OF_STOCK = 0
    STATUS_CHOICES = (
        (IN_STOCK, 'In stock'),
        (OUT_OF_STOCK, 'Out of stock')
    )
    status = models.PositiveIntegerField(
        choices=STATUS_CHOICES, default=IN_STOCK
    )
    product_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=200,)
    description = models.TextField(blank=True, null=True)
    product_image = models.FileField(null=True, blank=True)
    product_video = models.FileField(null=True, blank=True)
    tax = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    shipping_charge = models.IntegerField(null=True, blank=True)
    net_amount = models.IntegerField(null=True, blank=True)
    offer_percentage = models.IntegerField(null=True, blank=True)
    # category = models.ForeignKey(category)
    
    def __str__(self):
        return self.name
    