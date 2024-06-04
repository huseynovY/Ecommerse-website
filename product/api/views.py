from product.models import Category, Tag, Product, Color, Size
from django.http import JsonResponse
from product.api.serializers import CategorySerializer, TagSerializer, ProductSerializer, ColorSerializer, SizeSerializer, ProductCreateSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from product.models import Subscriber
from product.api.serializers import SubscriberSerializer

class SubscriberCreateApiView(CreateAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()

class CategoryApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

# def categories(request):
#     category_lists = Category.objects.all()
#     # category_dict = []
#     # for category in category_lists:
#     #     category_dict.append({
#     #         'category_id' : category.id,
#     #         'category_title' : category.title,
#     #     })

#     serializer = CategorySerializer(category_lists, many = True) 
#     return JsonResponse(serializer.data, safe = False)


class TagApiViews(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


# def tags(request):
#     tag_lists = Tag.objects.all()
#     seralizer = TagSerializer(tag_lists, many = True)
#     return JsonResponse(seralizer.data, safe = False)

class ColorApiView(ListAPIView):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
    
# def colors(request):
#     color_lists = Color.objects.all()
#     serializer = ColorSerializer(color_lists, many = True)
#     return JsonResponse(serializer.data, safe = False)

class SizeApiView(ListAPIView):
    serializer_class = SizeSerializer
    queryset = Size.objects.all()

# def sizes(request):
#     size_lists = Size.objects.all()
#     serializer = SizeSerializer(size_lists, many = True)
#     return JsonResponse(serializer.data, safe = False)

class ProductListCreateApiView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductCreateSerializer
        return self.serializer_class

# @api_view(http_method_names=["GET", "POST"])
# def products(request):
#     product_lists = Product.objects.all()
#     serializer = ProductSerializer(product_lists, many = True)
#     if request.method == "POST":
#         serializer = ProductCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe = False, status = 201)
#         return JsonResponse(serializer.errors, safe = False, status = 400)
#     product_lists = Product.objects.all()
#     serializer = ProductSerializer(product_lists, context = {'request':request} ,many = True)
#     return JsonResponse(serializer.data, safe = False)

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()


# @api_view(http_method_names=["PUT", "PATCH"])
# def product_update(request,pk):
#     if request.method == "PUT":
#         product = Product.objects.get(id = pk)
#         serializer = ProductCreateSerializer(data=request.data, instance = product)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe = False, status = 201)
#         return JsonResponse(serializer.errors, safe = False, status = 400)
#     if request.method == "PATCH":
#         product = Product.objects.get(id = pk)
#         serializer = ProductCreateSerializer(data=request.data, partial = True, instance = product)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe = False, status = 201)
#         return JsonResponse(serializer.errors, safe = False, status = 400)
#     return JsonResponse(serializer.data, safe = False)