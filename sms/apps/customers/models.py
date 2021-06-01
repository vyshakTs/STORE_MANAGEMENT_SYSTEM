from autoslug import AutoSlugField
from django.db import models

from sms.apps.accounts.models import (City, Country, PostCode, State,
                                  TimeStampedModel, User)


# Create your models here.
class CustomerProfile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    photo = models.FileField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    dob = models.DateTimeField('Date of birth')
    phone_no = models.IntegerField('Phone number')
    slug = AutoSlugField(unique=True, null=False,)
    current_address = models.TextField(blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True) # many-to-one relationship
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    post_code = models.ForeignKey(PostCode, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.user
    