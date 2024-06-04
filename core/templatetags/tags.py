from django.template import Library
register = Library()
from product.models import Category, Product

@register.simple_tag
def get_categories(limit):  
    categories = Category.objects.all()[:limit]
    return categories

@register.inclusion_tag('includes/recent_products.html')
def recent_products(limit = 5):
    products = Product.objects.order_by('-created_at')[:limit]
    return{
        'products' : products,
    }