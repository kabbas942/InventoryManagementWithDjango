from django.contrib import admin
from Management import models 
# Register your models here.
admin.site.register([models.Product,models.Order])
