from django.shortcuts import render,redirect
from cart.models.cart import Cart
from orders.models.orders import Order



def initial_order(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request, 'orders/initial_order.html', context={'carts':carts, 'order':order})
    else:
        return redirect("index")

    
