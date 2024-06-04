from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from product.models import Product, Category, Tag, Size, Color
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from product.forms import ProductCommentForm
from django.urls import reverse_lazy

def customerreview(request):
    return render(request, 'customer-review.html')

class ProductDetailView(FormMixin,DetailView):
    template_name = 'product-details.html'
    model = Product
    form_class = ProductCommentForm

    def get_success_url(self) -> str:
        return reverse_lazy( 'productdetails',kwargs = {'slug' : self.object.slug})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = self.get_object()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
  

    def form_valid(self, form: Any) -> HttpResponse:
        form.instance.user = self.request.user
        form.instance.product = self.object
        form.save()
        return super().form_valid(form)



        



# def productdetails(request, pk):
#     product = get_object_or_404(Product, id = pk)
#     categories = Category.objects.all()
#     product.view_count += 1
#     product.save()   
    
#     context = {
#         'product' : product,
#         'categories' : categories,
#     }
#     return render(request, 'product-details.html', context)




class ShopListView(ListView):
    template_name = 'shop.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 8

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['sizes'] = Size.objects.all()
        context['colors'] = Color.objects.all()
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        search = self.request.GET.get('searched')
        size = self.request.GET.get('size')
        color = self.request.GET.get('color')

        if search:
            queryset = queryset.filter(title__icontains = search)
        if category:
            queryset = queryset.filter(category__id = category)
        if tag:
            queryset = queryset.filter(tags__id = tag)
        if size:
            queryset = queryset.filter(size__id = size)
        if color:
            queryset = queryset.filter(color__id = color)
        if tag and category:
            queryset = queryset.filter(category__id = category, tags__id = tag)
        return queryset
    

# def shop(request):
#     print(request.session.get('liked_posts'))
#     products = Product.objects.all()
#     categories = Category.objects.all()
    

#     context = {
#         'product_list' : products,
#         'categories' : categories,
#     }
#     return render(request,'shop.html', context)

# def like_post(request, pk):
#     messages.add_message(request, messages.SUCCESS, 'Liked!')
#     request.session['liked_posts'] = request.session.get('liked_posts',' ') + str(pk) + ' '
    
#     return render(request, 'shop.html')