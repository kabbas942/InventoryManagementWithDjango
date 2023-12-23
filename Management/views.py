from django.shortcuts import render,redirect
from Management import models
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"Management/index.html")

def product(request):
    productsInfo = models.Product.objects.all()
    ProductDictionary = {'ProductInfo':productsInfo}
    return render(request,"Management/product.html",ProductDictionary)

def productDelete(request,productDeleteId):
    print(productDeleteId)
    productInfo = models.Product.objects.get(id=productDeleteId)
    productInfo.delete()
    messages.success(request,"Product Deleted successfully")
    return redirect("/product")
