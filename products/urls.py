from django.contrib import admin
from django.urls import path, include
from products.views.products import index
from products.views.product_details import product_detail




#app_name='products'

urlpatterns = [
    path('', index, name='index'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),

]