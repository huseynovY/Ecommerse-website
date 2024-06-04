from django.contrib import admin
from order.models import Order, Wishlist, OrderItem
# Register your models here.
admin.site.register(Order)
admin.site.register(Wishlist)
admin.site.register(OrderItem)