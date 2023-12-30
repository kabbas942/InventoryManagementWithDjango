from django.contrib import admin
from django.urls import path
from Account import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('',LoginView.as_view(template_name='Account/login.html'),name="user-login"),
    path('signup',views.signup,name="signup")
]
