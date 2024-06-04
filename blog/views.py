from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from blog.models import Blog, Blogcategory, Blogtag
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from blog.forms import BlogCommentForm
from django.urls import reverse_lazy

# Create your views here.

class BlogDetailView(FormMixin, DetailView):
    template_name = 'blog-details.html'
    model = Blog
    form_class = BlogCommentForm  
    slug_field ='slug'  
    slug_url_kwarg = 'slug'
    # success_url = reverse_lazy('home')

    def get_success_url(self) -> str:
        return reverse_lazy('blog-details', kwargs = {'slug' : self.object.slug})


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tags'] = Blogtag.objects.all()
        context['categories'] = Blogcategory.objects.all()
        
        arr = self.request.session.get('reently_viewed', [])
        slug = self.kwargs['slug']  
        
        if slug in arr:
            arr.remove(slug)
            recently_viewed_blogs = Blog.objects.filter(slug__in=arr)
        else:
            recently_viewed_blogs = Blog.objects.filter(slug__in=arr)
            arr.append(slug)
            self.request.session['recently_viewed'] = arr

        context['recently_viewed_blogs'] = recently_viewed_blogs

        return context 
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = self.get_object()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

        
    def form_valid(self, form: Any) -> HttpResponse:
        form.instance.user = self.request.user
        form.instance.blog = self.object
        form.save()
        return super().form_valid(form)
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        search = self.request.GET.get('searched')
       
        if search:
            queryset = queryset.filter(title__icontains = search)
        if category:
            queryset = queryset.filter(category__id = category)
        if tag:
            queryset = queryset.filter(tags__id = tag)
        if tag and category:
            queryset = queryset.filter(category__id = category, tags__id = tag)
        return queryset

    
    
    
# def blogdetails(request, pk):
#     blog = get_object_or_404(Blog, id = pk)
#     categories = Blogcategory.objects.all()
#     tags = Blogtag.objects.all()

#     arr =  request.session.get('recently_viewed', [])
    
#     if pk in arr:
#         arr.remove(pk)
#         recently_viewed_blogs = Blog.objects.filter(pk__in = arr)
#     else:
#         recently_viewed_blogs = Blog.objects.filter(pk__in = arr)
#         arr.append(pk)
#         request.session['recently_viewed'] = arr
    
#     context = {
#         'blog' : blog,
#         'categories' : categories,
#         'tags' : tags,
#         'recently_viewed_blogs' : recently_viewed_blogs,
#     }
#     return render(request, 'blog-details.html', context)


def team(request):
    return render(request, 'team.html')

class BlogListView(ListView):
    template_name = 'blog.html'
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 9
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Blogcategory.objects.all()
        return context
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        if category:
            queryset = queryset.filter(category__id = category)
        if tag:
            queryset = queryset.filter(tags__id = tag)
        if tag and category:
            queryset = queryset.filter(category__id = category, tags__id = tag)
        return queryset
    


# def blog(request):
#     blogs = Blog.objects.all()
#     categories = Blogcategory.objects.all()

#     context = {
#         'blog_list' : blogs,
#         'categories' : categories,
#     }
#     return render(request, 'blog.html', context )