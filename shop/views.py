from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from.models import Category, Product

# Create your views here.

def allProdCat(request, category_id=None):
    c_page = None
    products = None
    if category_id != None:
        c_page = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=c_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)

    return render(request,'shop/category.html',{'category':c_page,'products':products})