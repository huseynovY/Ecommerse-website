from django.db import models
from core.models import Abstractmodel
from django.contrib.auth import get_user_model
User=get_user_model()
from product.models import Product
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    def __str__(self) -> str:
        return f"{self.product}"
    


class Basket(Abstractmodel):
    user = models.ForeignKey(User, related_name='basket', on_delete=models.CASCADE)
    basket_items = models.ForeignKey('BasketItems', related_name='baskets', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)


class BasketItems(Abstractmodel):
    product = models.ForeignKey(Product, related_name='basketitems', on_delete=models.CASCADE)
    quantity = models.IntegerField('quantity')

class Wishlist(Abstractmodel):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    

     def __str__(self) -> str:
         return f"{self.product}"