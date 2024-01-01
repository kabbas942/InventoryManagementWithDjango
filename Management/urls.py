from django.urls import path
from Management import views

urlpatterns = [
    path('',views.index,name="Dashboard"),
    path('product',views.product,name="ProductLink"),
    path('productdelete/<int:productDeleteId>/',views.productDelete,name="productDeleteLink"),
    path('updateProduct/<int:updateProductId>/',views.updateProduct,name="updateProductLink"),
]