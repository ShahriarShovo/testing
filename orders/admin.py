from django.contrib import admin
from orders.models.orders import Order
from orders.models.billing_address import BillingAddress

# Register your models here.
admin.site.register(Order)
admin.site.register(BillingAddress)
