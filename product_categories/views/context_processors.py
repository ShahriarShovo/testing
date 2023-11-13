from product_categories.models.models import Product_Categories

def categories(request):

    category_name = Product_Categories.objects.all()
    
    return {'category_name' : category_name}