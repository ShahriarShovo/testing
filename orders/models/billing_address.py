from django.db import models
from django.conf import settings

# Create your models here.

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=200, blank=True)
    house_number = models.CharField(max_length=20, blank=True)
    street = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f'{self.user.email} billing address' 