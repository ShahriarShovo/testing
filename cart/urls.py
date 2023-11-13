from django.urls import path, include
from cart.views.cart import add_to_cart
from cart.views.cart_view import cart_view
from cart.views.increase_item import increase_cart
from cart.views.decrease_item import decrease_cart
from cart.views.remove_item import remove_from_cart




urlpatterns = [
    
     path('add/<int:pk>/', add_to_cart, name='add_to_cart'), 
     path('view/', cart_view, name='cart_view'),
     path('increase_item/<pk>/', increase_cart, name="increase_item"),
     path('decrease_item/<pk>/', decrease_cart, name="decrease_item"),
     path('remove/<int:pk>/', remove_from_cart, name='remove_from_cart'),
     path('check_out/', include('orders.urls')),

]
