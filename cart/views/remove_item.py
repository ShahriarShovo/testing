from django.shortcuts import render, get_object_or_404 , redirect
from cart.models.cart import Cart
from orders.models.orders import Order
from products.models.models import Products


def remove_from_cart(request,pk):
    item = get_object_or_404(Products, pk=pk)
    order_qs = Order.objects.filter(user= request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderItems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            order.orderItems.remove(order_item)
            order_item.delete()
            return redirect("cart_view")
        else:
            return redirect("index")

    else:
       
        return redirect("index")