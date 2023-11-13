from django.db import models
from product_categories.models.models import Product_Categories

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='products')
    product_price = models.FloatField()
    product_old_price = models.FloatField()
    product_brand = models.CharField(max_length=50)
    product_discription = models.TextField()

    product_category = models.ForeignKey(Product_Categories, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product_name
