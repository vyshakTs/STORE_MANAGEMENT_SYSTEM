import uuid

from django.db import models

from sms.apps.accounts.models import TimeStampedModel


# Create your models here.
class Orders(TimeStampedModel):
    webstore = models.ForeignKey('storemaster.WebStore', on_delete=models.CASCADE, blank=True, null=True)
    order_id = models.UUIDField(default=uuid.uuid4)
    products = models.ManyToManyField('OrderProducts', related_name='ordered_products',)
    customer = models.ForeignKey('customers.CustomerProfile', on_delete=models.SET_NULL, blank=True, null=True)
    PENDING = 1
    OUT_FOR_DELIVERY = 2
    DELIVERED = 3
    status_choices = (
        (PENDING, 'pending'),
        (OUT_FOR_DELIVERY, 'out for delivery'),
        (DELIVERED, 'delivered'),
    )
    status = models.PositiveIntegerField(
        choices = status_choices, default=PENDING,
    )
    
    def __str__(self):
        return self.products.products.name

class OrderProducts(models.Model):
    # order = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ForeignKey('products.Product', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    
    def __str__(self):
        return self.products.name
    