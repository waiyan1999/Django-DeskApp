from django.urls import path
from myapp.views import *

urlpatterns = [
    path('base/',base, name = 'base'),
    path('', index , name = 'index'),
    path('product/',product , name = 'product'),
    path('login/', loginView , name = 'login'),
    path('register/', registerView , name = 'register'),
    path('productdetail/<int:id>/',productDetail, name = 'productdetail'),
    path('deleteproduct/<int:id>/',deleteProduct, name = 'deleteproduct'),
    path('editproduct/<int:id>',editProduct , name ="editproduct" ),
    path('productlist/', listProduct ,name = 'productlist')
]