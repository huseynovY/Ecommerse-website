from django.urls import path
from blog.api.views import BlogCategoryListApiView, BlogTagListAPIView, BlogListCreateAPIView, BlogRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('blogcategories/', BlogCategoryListApiView.as_view(), name = ('blogcategories')),
    path('blogtags/', BlogTagListAPIView.as_view(), name = ('blogtags')),
    path('blogs/', BlogListCreateAPIView.as_view(), name = ('blogs')),
    path('blog/<int:pk>/', BlogRetrieveUpdateDestroyAPIView.as_view(), name = 'blog_update'),
]
