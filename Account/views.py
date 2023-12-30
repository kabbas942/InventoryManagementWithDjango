from django.shortcuts import render
from .forms import userform
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field,Submit
# Create your views here.

def signup(request):
    form= userform()
    return render(request,"Account/signup.html",{'form':form})