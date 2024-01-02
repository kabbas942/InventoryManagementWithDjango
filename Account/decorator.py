from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User,Group

def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper(request,*args, **kwargs):
            group = None
            if Group.objects.exists():
                group = Group.objects.all()
                print(group)
                return view_func(request,*args, **kwargs)
            else:
                print(group)
                return view_func(request,*args, **kwargs)
                
        return wrapper
    return decorators