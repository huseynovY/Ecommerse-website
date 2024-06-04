from django.shortcuts import render
from order.models import Wishlist, OrderItem, Order
# Create your views here.


def cart(request):
    product=Order.objects.filter()
    product=OrderItem.objects.filter(order__customer=request.user)
    subtotal = sum(item.product.price for item in product)

    print(product,"ASDfsaf")
    context={
        'product' : product,
        'subtotal' : subtotal,
    }
    return render(request, 'cart.html',context)

def checkout(request):
    return render(request, 'checkout.html')

def wishlist(request):
    products = Wishlist.objects.filter(user=request.user)
    print(products, "ASDdqwas")
    
    context = {
        'products': products,
    }

    return render(request, 'wishlist.html', context)