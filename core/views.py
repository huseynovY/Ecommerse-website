from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.forms import ContactForm
from django.contrib import messages
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _
from core.tasks import export_data
from product.models import Product, Color
from blog.models import Blog, Blogcategory

from product.models import Category

from order.models import Order, OrderItem
# Create your views here.
def about(request):
    blogs = Blog.objects.all()[0:6]

    context = {
        'blogs' : blogs,
    }
    return render(request, 'about.html', context)

class Contactview(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.add_message(self.request, messages.SUCCESS, _('Successfully sent!'))
        return super().form_valid(form)
    
# def contact(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(data = request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, 'Successfully sent!')
#             return redirect(reverse_lazy('contact'))


#     context = {
#         'form' : form,
#     }
#     return render(request, 'contact.html', context)

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    colors = Color.objects.all()
    blogs = Blog.objects.all()[0:6]
    blogcategories = Blogcategory.objects.all()

    new_blogs = Blog.objects.all()[0:3]
    best_blogs = Blog.objects.all()[3:6]
    top_rated_blogs = Blog.objects.all()[6:9]
    interesting_blogs = Blog.objects.all()[9:12] 

    new_products=Product.objects.order_by("-created_at")
    best_sale=Product.objects.all()[4:8]
    top_rated=Product.objects.all()[8:12]
    on_sale=Product.objects.all()[12:16]

    productss=Order.objects.filter()
    productss=OrderItem.objects.filter(order__customer=request.user)
    subtotal = sum(item.product.price for item in productss)

    print(productss,"ASDfsaf")

    context = {
        'categories' : categories,
        'products' : products,
        'colors' : colors,  
        'blogs' : blogs,
        'new_products' : new_products,
        'best_sale' : best_sale,
        'top_rated' : top_rated,
        'on_sale' : on_sale,
        'blogcategories' : blogcategories,
        'new_blogs' : new_blogs,
        'best_blogs' : best_blogs,
        'top_rated_blogs' : top_rated_blogs,
        'interesting_blogs' : interesting_blogs,
        'productss' : productss,
        'subtotal' : subtotal,
    }
    return render(request, 'index.html', context)

def export(request):
    export_data.delay()
    return HttpResponse('Success!')   