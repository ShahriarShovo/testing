from django.db import models
from user_auth.models.user import User


class Profile(models.Model):
    user                       =                    models.OneToOneField(User, on_delete=models.CASCADE,                                                                   related_name='profile')
    address                    =                    models.TextField(max_length=300, blank=True)
    zipcode                    =                    models.CharField(max_length=10, blank=True)
    date_joined                =                    models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username + "'s Profile"