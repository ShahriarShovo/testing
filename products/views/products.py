from django.shortcuts import render
from products.models.models import Products

# Create your views here.

def index(request):

    fatch_all_products = Products.objects.all()
    context ={
        'fatch_all_products' : fatch_all_products,
    }
    
    return render(request, 'index/index.html', context=context)

def product_detail(request):
    return render(request, 'product_page/product_details.html')
