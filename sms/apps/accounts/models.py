import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import F
from phonenumber_field.modelfields import PhoneNumberField

from apps.storemaster.models import WebStore
from helpers import current_datetime


# Create your models here.
class TimeStampedModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    user_id = models.UUIDField(null=True)
    STORE_OWNER = 1
    EMPLOYEE = 2
    CUSTOMER = 3
    USER_TYPE_CHOICES = (
        (CUSTOMER, 'customer'),
        (STORE_OWNER, 'store owner'),
        (EMPLOYEE, 'employee'),
    )
    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, default=CUSTOMER
    )
    is_first_login = models.BooleanField(default=True)
    mobile = PhoneNumberField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def is_CUSTOMER(self):
        return self.user_type == self.CUSTOMER

    @property
    def is_EMPLOYEE(self):
        return self.user_type == self.EMPLOYEE

    @property
    def is_SO(self):
        return self.user_type == self.STORE_OWNER

    # def save(self, *args, **kwargs):
    #     created = self.pk is None
    #     super(User, self).save(*args, **kwargs)
    #     if created and self.is_SO:
    #         WebStore.objects.create(user=self)


class PostCode(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, default=None)
    pin_code = models.CharField(max_length=50)


class City(models.Model):
    city_id = models.UUIDField(default=uuid.uuid4)
    state = models.ForeignKey('State', on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)
    city_code = models.CharField(max_length=10, unique=True)


class State(models.Model):
    state_id = models.UUIDField(default=uuid.uuid4)
    country = models.ForeignKey('Country', on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)
    state_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    country_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    pass
