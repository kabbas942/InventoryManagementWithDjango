from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"Management/index.html")

def product(request):
    return render(request,"Management/product.html")