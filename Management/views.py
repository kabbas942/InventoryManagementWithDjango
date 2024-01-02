from django.shortcuts import render,redirect
from Management import models
from django.forms.models import model_to_dict
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Management.forms import ProductForm
from Account.decorator import allowed_users
from django.contrib.auth.models import User,Group
# Create your views here.
@login_required(login_url='user-login')
def index(request):
    return render(request,"Management/index.html")

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
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

@login_required(login_url='user-login')
def productDelete(request,productDeleteId):
    print(productDeleteId)
    productInfo = models.Product.objects.get(id=productDeleteId)
   
    if productInfo.delete():
        messages.success(request,"Product Deleted successfully")
    else:
        messages.warning(request,"Product Deletion unsuccessful.")
    return redirect("/Management/product")

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['viewers'])
def updateProduct(request,updateProductId):
    Record=models.Product.objects.get(id=updateProductId)

    if request.method=="POST":
        form = ProductForm(request.POST,instance=Record)
        if form.is_valid():
            form.save()
            messages.success(request,"Product Updated successfully.")
        else:
            messages.warning(request,"Product Updation Unsuccessful.")
        return redirect("/Managament/product")
    else:
        form = ProductForm(initial=model_to_dict(Record))
    return render(request,"Management/updateProduct.html",{'form':form})


