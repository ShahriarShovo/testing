from django.shortcuts import render
from products.models.models import Products

# Create your views here.



def product_detail(request, pk):

    product_details = Products.objects.get(pk=pk)

    context={
        'product_details' : product_details,
    }

    return render(request, 'product_page/product_details.html', context=context)