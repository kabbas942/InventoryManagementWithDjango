from django.shortcuts import render,redirect
from Management import models
from django.contrib import messages
from Management.forms import ProductForm
# Create your views here.
def index(request):
    return render(request,"Management/index.html")

def product(request):
    productsInfo = models.Product.objects.all()
    if request.method=="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    ProductDictionary = {'ProductInfo':productsInfo,'form':form}
    return render(request,"Management/product.html",ProductDictionary)

def productDelete(request,productDeleteId):
    print(productDeleteId)
    productInfo = models.Product.objects.get(id=productDeleteId)
    productInfo.delete()
    messages.success(request,"Product Deleted successfully")
    return redirect("/product")

def updateProduct(request,updateProductId):
    if request.method=="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    return render(request,"Management/updateProduct.html",{'form':form})

