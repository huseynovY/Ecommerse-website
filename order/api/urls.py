from django.urls import path
from .views import WishlistListCreateView, OrderItemListCreateView , OrderListCreateView

urlpatterns = [
    path('wishlist/', WishlistListCreateView.as_view(), name=('wishlist')),
    path('orders/', OrderListCreateView.as_view(), name='orders'),
    path('order-items/', OrderItemListCreateView.as_view(), name='order-items'),
]

