from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
from core.models import Abstractmodel
from django.urls import reverse_lazy

# Create your models here.


class Product(Abstractmodel):
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='products')
    size = models.ManyToManyField('Size', related_name='products')
    color = models.ManyToManyField('Color', related_name='products')
    user = models.ForeignKey(User, related_name = 'products', on_delete = models.CASCADE)

    title = models.CharField('title', max_length=100)
    image = models.ImageField('image', upload_to='product_image/', null=True, blank=True)
    cover_image = models.ImageField('cover_image', upload_to='product_image/')
    price = models.DecimalField('price', max_digits=7, decimal_places=2)
    smalldescription = models.TextField('smalldescription', max_length=50)
    description = models.TextField('description', max_length=1000)
    slug = models.SlugField('slug', max_length=200, null=True, blank=True)
    view_count = models.IntegerField('view_count', default = 0)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse_lazy('productdetails', kwargs = {'slug' : self.slug})




class ProductComment(Abstractmodel):
    parent = models.ForeignKey('self', related_name = 'children', on_delete= models.CASCADE, null = True, blank = True)
    user = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='comment', on_delete=models.CASCADE)
    message =  models.TextField()
    
    def __str__(self) -> str:
        return f'{self.user.username} / {self.product}'

class ProductImage(Abstractmodel):
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField('image', upload_to='product_images/')

    def __str__(self) -> str:
        return self.product.title


class Category(Abstractmodel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True )
    title = models.CharField('title', max_length=100)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self) -> str:
        if self.parent:  
             return f'{self.parent} - {self.title}'
        return self.title

class Tag(Abstractmodel):
    title = models.CharField('title', max_length=100)

    def __str__(self) -> str:
        return self.title

class Size(Abstractmodel):
    title = models.CharField('title', max_length=20)
    def __str__(self) -> str:
        return self.title

class Color(Abstractmodel):
    title = models.CharField('title', max_length=100)
    hex_code = models.CharField('Hex Code', max_length=7, default='#000000')


    def __str__(self) -> str:
        return self.title



class Subscriber(Abstractmodel):
    email = models.EmailField(max_length = 50, unique = True)

    def __str__(self) -> str:
        return self.email

# class ProductVersion(Abstractmodel):
#     color = models.ManyToManyField(Product, related_name='products')
#     size = models.ManyToManyField(Product , related_name='products')
#     tag = models.ManyToManyField(Product, related_name='products')
#     user = models.ForeignKey(User, related_name = 'products', on_delete = models.CASCADE)

#     title = models.CharField('title', max_length = 100)
