from django.shortcuts import render,redirect
from Management import models
# Create your views here.
def index(request):
    return render(request,"Management/index.html")

def product(request):
    ProductInfo = models.Product.objects.all()
    ProductDictionary = {'ProductInfo':ProductInfo}
    print(ProductInfo)
    return render(request,"Management/product.html",ProductDictionary)

def productDelete(request,productDeleteId):
    print(productDeleteId)
    return redirect("/product")
