from django.urls import path
from product.views import customerreview, ProductDetailView, ShopListView

urlpatterns = [
    path('customerreview/', customerreview, name=('customerreview')),
    path('productdetails/<str:slug>/', ProductDetailView.as_view(), name=('productdetails')),
    path('shop/', ShopListView.as_view(), name=('shop')),
    # path('like_post/<int:pk>/', like_post, name=('like_post'))
]
