from django.shortcuts import render,redirect
from .forms import userform
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field,Submit
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.method=="POST":
        form = userform(request.POST)
        if form.is_valid():
            form.save()
            message=messages.success(request,"Account Created Successfully")
            return redirect('/')
        else:
            message=messages.warning(request,"Account Creation failed")
    else:
        form= userform()
    return render(request,"Account/signup.html",{'form':form})