from product.models import Category, Tag, Product, Color, Size
from rest_framework import serializers
from product.models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('email',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title', 
    )
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'title',
        )

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            'id',
            'title'
        )

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            'id',
            'title'
        )



class ProductSerializer(serializers.ModelSerializer):

    # category = serializers.CharField(source = 'category.title')
    category = CategorySerializer()
    tags = TagSerializer(many = True)
    color = ColorSerializer(many = True)
    size = SizeSerializer(many = True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'category',
            'tags',
            'color',
            'size',
            'price',
            'smalldescription',
            'description',
            'view_count',
            'image',
            'cover_image',
            'slug',
        )


class ProductCreateSerializer(serializers.ModelSerializer):

    # category = serializers.CharField(source = 'category.title')
    # category = CategorySerializer()
    # tags = TagSerializer(many = True)
    # color = ColorSerializer(many = True)
    # size = SizeSerializer(many = True)
    user = serializers.PrimaryKeyRelatedField(read_only = True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'category',
            'tags',
            'user',
            'color',
            'size',
            'price',
            'smalldescription',
            'description',
            'view_count',
            'image',
            'cover_image',
            'slug',
        )


    def validate(self, attrs):
        request = self.context['request']
        attrs['user'] = request.user
        return super().validate(attrs)