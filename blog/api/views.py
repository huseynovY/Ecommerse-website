from blog.models import Blogcategory, Blogtag, Blog
from django.http import JsonResponse
from blog.api.serializers import BlogCategorySeriazlizer, BlogTagSerializer, BlogSerializers, BlogCreateSerializers
from rest_framework.generics import ListAPIView , ListCreateAPIView, RetrieveUpdateDestroyAPIView


class BlogCategoryListApiView(ListAPIView):
    serializer_class = BlogCategorySeriazlizer
    queryset = Blogcategory.objects.all()

# def blogcategories(request):
#     blogcategory_lists = Blogcategory.objects.all()
#     serializers = BlogCategorySeriazlizer(blogcategory_lists, many = True)
#     return JsonResponse(serializers.data, safe = False)

class BlogTagListAPIView(ListAPIView):
    serializer_class = BlogTagSerializer
    queryset = Blogtag.objects.all()
    

# def blogtags(request):
#     blogtag_lists = Blogtag.objects.all()
#     serializers = BlogTagSerializer(blogtag_lists, many = True)
#     return JsonResponse(serializers.data, safe = False) 

class BlogListCreateAPIView(ListCreateAPIView):
    serializer_class = BlogSerializers
    queryset = Blog.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BlogCreateSerializers
        return self.serializer_class

# def blogs(request):
#     blog_lists = Blog.objects.all()
#     serializers = BlogSerializers(blog_lists, many = True)
#     return JsonResponse(serializers.data, safe = False)

class BlogRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogCreateSerializers
    queryset = Blog.objects.all()