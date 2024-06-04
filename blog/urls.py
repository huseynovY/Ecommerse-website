from django.urls import path
from blog.views import BlogDetailView, BlogListView, team

urlpatterns = [
    path('blog-details/<str:slug>/', BlogDetailView.as_view(), name= 'blog-details'), 
    path('blog/', BlogListView.as_view(), name= 'blog'),
    path('team/', team, name='team')
]
