from blog.models import Blogcategory, Blogtag, Blog
from rest_framework import serializers

class BlogCategorySeriazlizer(serializers.ModelSerializer):
    class Meta:
        model = Blogcategory
        fields = (
            'id',
            'title'
        )

class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogtag
        fields = (
            'id',
            'title'
        )

class BlogSerializers(serializers.ModelSerializer):

    category = BlogCategorySeriazlizer()
    tags = BlogTagSerializer(many = True)

    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'user',
            'category',
            'tags',
            'image',
            'slug',
            'smalldescription',
            'description'
        )


class BlogCreateSerializers(serializers.ModelSerializer):

    # category = BlogCategorySeriazlizer()
    # tags = BlogTagSerializer(many = True)

    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'user',
            'category',
            'tags',
            'image',
            'slug',
            'smalldescription',
            'description'
        )