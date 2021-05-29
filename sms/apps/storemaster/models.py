import uuid

from django.db import models
from django.db.models import Q

# Create your models here.
# class TimeStampedModel(models.Model):
#     created_date = models.DateTimeField(auto_now_add=True)
#     modified_date = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True
        

class WebStore(models.Model):
    # language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(
        'accounts.User', on_delete=models.CASCADE, primary_key=True)
    store_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=50, unique=True)
    # url = models.URLField(max_length=200, unique=True)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.ForeignKey('accounts.City', on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey('accounts.State', on_delete=models.SET_NULL, null=True, blank=True)
    country = models.ForeignKey('accounts.Country', on_delete=models.SET_NULL, null=True, blank=True)
    post_code = models.ForeignKey(
        'accounts.PostCode', on_delete=models.SET_NULL, null=True, blank=True)
    phone_no = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
    
    @property
    def is_complete(self):
        if self.objects.filter(Q(user__isnull=True) | Q(name__isnull=True) | Q(address1__isnull=True) | Q(phone_no__isnull=True)):
            return False
        else:
            return True
