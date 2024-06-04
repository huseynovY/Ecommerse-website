from order.models import Wishlist, Order, OrderItem
from rest_framework import serializers


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = (
            'product',
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'customer',
            'complete',
            'transaction_id'
        )


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'product' ,
            'order',
            'quantity'
        )

    def save(self, **kwargs):
        return super().save(**kwargs)
