from order.models import Wishlist , Order, OrderItem
from order.api.serializers import WishlistSerializer , OrderItemSerializer, OrderSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class WishlistListCreateView(ListCreateAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        print(self.request.user)

        existing_wishlist = Wishlist.objects.filter(user = self.request.user, product = serializer.validated_data['product']).first()

        if existing_wishlist:
            pass
        else:
           serializer.save(user=self.request.user, product = serializer.validated_data['product'])


class OrderListCreateView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrderItemListCreateView(ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        order=Order.objects.get(customer=self.request.user)
        existing_order_item = OrderItem.objects.filter(order=order, product=serializer.validated_data['product']).first()
        print(existing_order_item)
        if existing_order_item:
              existing_order_item.quantity += 1
              existing_order_item.save()
        else:
          serializer.save(order=order, quantity=1) 
