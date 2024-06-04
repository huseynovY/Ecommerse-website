from django.urls import path
from core.views import about , Contactview, home, export

urlpatterns = [
    path('about/', about, name= 'about'),
    path('contact/', Contactview.as_view(), name= 'contact'),
    path('', home, name=('home')),
    path('export/', export, name= 'export'),
]
