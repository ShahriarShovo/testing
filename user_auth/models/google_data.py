from django.db import models
from user_auth.models.user import User

class Google_Data(models.Model):
   
    google_user_id = models.CharField(max_length=100, blank=True,null=True)
    user_email = models.EmailField(max_length=254)
    verified_email = models.BooleanField(null=True)
    user_name = models.CharField(max_length=100, blank=True,null=True)
    user_given_name = models.CharField(max_length=100, blank=True,null=True)
    user_family_name = models.CharField(max_length=100, blank=True,null=True)
    user_picture = models.URLField()
    user_language = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        verbose_name = ("Google Data")
        

    def __str__(self):
        return self.user_email

    