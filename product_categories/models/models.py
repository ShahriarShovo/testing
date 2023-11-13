from django.db import models

# Create your models here.

class Product_Categories(models.Model):
    category_name = models.CharField(max_length=50)
    category_created = models.DateTimeField(auto_now=True)
    category_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.category_name