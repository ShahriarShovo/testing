from django.shortcuts import render, get_object_or_404 , redirect
from cart.models.cart import Cart
from orders.models.orders import Order
from products.models.models import Products



# Create your views here.

def add_to_cart(request, pk):
    item = get_object_or_404(Products, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user= request.user, purchased = False)
    order_qs = Order.objects.filter(user = request.user , ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderItems.filter(item=item).exists():
            order_item[0].quantity +=1
            order_item[0].save()
            return redirect("index")
        else:
            order.orderItems.add(order_item[0])
            return redirect("index")

    else:
        order = Order(user= request.user)
        order.save()
        order.orderItems.add(order_item[0])
        return redirect("index")








