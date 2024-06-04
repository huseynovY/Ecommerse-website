from django.urls import path
from product.api.views import  TagApiViews, ProductListCreateApiView, ColorApiView, SizeApiView, ProductRetrieveUpdateDestroyAPIView,CategoryApiView, SubscriberCreateApiView

urlpatterns = [
    path('categories/', CategoryApiView.as_view(), name = 'categories'),
    path('tags/', TagApiViews.as_view(), name = 'tags'),
    path('products/', ProductListCreateApiView.as_view(), name = 'products'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name = 'product_update'),
    path('colors/', ColorApiView.as_view(), name = ('colors')),
    path('sizes/', SizeApiView.as_view(), name = ('sizes')),
    path('subscriber/', SubscriberCreateApiView.as_view(), name = ('subscriber')),
]
 