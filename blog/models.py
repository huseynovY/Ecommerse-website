from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from core.models import Abstractmodel
from django.urls import reverse_lazy
# Create your models here.

class Blogcategory(Abstractmodel):
    title = models.CharField('title', max_length=100)
    
    class Meta:
        verbose_name_plural = 'Blogcategories'
    def __str__(self) -> str:
        return self.title
    
class Blogtag(Abstractmodel):
    title =  models.CharField('title', max_length=100)

    def __str__(self) -> str:
        return self.title
    
class Blog(Abstractmodel):
    category = models.ForeignKey('Blogcategory', related_name='blogs', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Blogtag', related_name='blogs')
    user = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)

    title = models.CharField('title', max_length=100)
    image = models.ImageField('image', upload_to='image/', null=True, blank=True)
    slug = models.SlugField('slug', max_length = 250, null = True, blank = True)
    smalldescription = models.TextField('smalldescription', max_length=100)
    description = models.TextField('description', max_length=1000)
    status = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('blog-details', kwargs = {'slug' : self.slug})
    
    class Meta:
        ordering = ['-created_at']
    
    


class BLogComment(Abstractmodel):
    parent = models.ForeignKey('self', related_name = 'children', on_delete= models.CASCADE, null = True, blank = True)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    message =  models.TextField()
    
    def __str__(self) -> str:
        return f'{self.user.username} / {self.blog}'
    
