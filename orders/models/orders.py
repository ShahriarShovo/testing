from django.db import models
from products.models.models import Products
from cart.models.cart import Cart
from django.conf import settings

class Order(models.Model):
    orderItems = models.ManyToManyField(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=264, blank=True, null=True)
    orderId = models.CharField(max_length=200, blank=True, null=True)

    def get_totals(self):
        total = 0
        for order_item in self.orderItems.all():
            total+= float(order_item.get_total())
        return total