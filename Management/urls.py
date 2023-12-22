from django.urls import path
from Management import views

urlpatterns = [
    path('',views.index,name="Dashboard"),
    path('product',views.product,name="Product")
]