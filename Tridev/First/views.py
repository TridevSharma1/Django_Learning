from django.shortcuts import render
from .models import *  ## Importing all models from the current app's models.py file

def category_products(request):
    categories = Category.objects.prefetch_related('products').all()
    return render(request, 'category_products.html', {'categories': categories})

def category_list(request):
    categories = Category.objects.all()
    
    context = {
        'categories': categories
    }
    
    return render(request, 'category_list.html', context)

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
