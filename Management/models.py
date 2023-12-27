from django.db import models
from django.contrib.auth.models import User
CATEGORY = (("Stationary","Stationary"),
            ("Electronics","Electronics"),
            ("Food","Food"))
# Create your models here.
class Product(models.Model):
    ProductName=models.CharField(max_length=100,null=True)
    ProductCategories= models.CharField(max_length=50,choices=CATEGORY,null=True)
    ProductPrice=models.PositiveBigIntegerField(null=True)
    ProductQty=models.PositiveBigIntegerField(null=True)

    def __str__(self):
        return f'{self.ProductName}'

    #Product Name 	Categories 	Prices 	Actions

class Order(models.Model):
    OrderId = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    CustomerId = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    PlacementTime = models.DateField(auto_now=True)
    def __str__(self):
        return f'{self.CustomerId}-{self.OrderId}'