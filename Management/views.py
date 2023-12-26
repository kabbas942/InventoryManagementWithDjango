from django.shortcuts import render,redirect
from Management import models
from django.forms.models import model_to_dict
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
            messages.success(request,"Product Added successfully")
        else:
            messages.warning(request,"Product Addition Unsuccessful.")
    else:
        form = ProductForm()
    ProductDictionary = {'ProductInfo':productsInfo,'form':form}
    return render(request,"Management/product.html",ProductDictionary)

def productDelete(request,productDeleteId):
    print(productDeleteId)
    productInfo = models.Product.objects.get(id=productDeleteId)
    if productInfo.delete():
        messages.success(request,"Product Deleted successfully")
    else:
        messages.warning(request,"Product Deletion unsuccessful.")
    return redirect("/product")

def updateProduct(request,updateProductId):
    Record=models.Product.objects.get(id=updateProductId)
    if request.method=="POST":
        form = ProductForm(request.POST,instance=Record)
        if form.is_valid():
            form.save()
            messages.success(request,"Product Updated successfully.")
        else:
            messages.warning(request,"Product Updation Unsuccessful.")
        return redirect("/product")
    else:
        form = ProductForm(initial=model_to_dict(Record))
    return render(request,"Management/updateProduct.html",{'form':form})

