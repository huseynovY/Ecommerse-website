from django.contrib import admin
from product.models import Product, Category, Tag, Color, Size,  ProductImage ,ProductComment, Subscriber
from django import forms
from modeltranslation.admin import TranslationAdmin
# Register your models here.


admin.site.register(Size)
admin.site.register(ProductComment)
admin.site.register(ProductImage)
admin.site.register(Subscriber)

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    fields = 'title','parent'


@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    fields = 'title', 


@admin.register(Color)
class ColorAdmin(TranslationAdmin):
    fields = 'title','hex_code'

class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'tags' : forms.CheckboxSelectMultiple,
            'color' : forms.CheckboxSelectMultiple,
            'size' : forms.CheckboxSelectMultiple,

            
        }

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'get_tags']
    list_display_links = ['id', 'title']
    list_editable = ['category']
    list_filter = ['category']
    search_fields = ['title', 'category__title']
    inlines = [ProductImageAdmin]
    # prepopulated_fields = {
    #     'slug' : ('title',)
    # }
    form = ProductAdminForm

    def get_tags(self, obj):
        tags = []
        for tag in obj.tags.all():
            tags.append(tag)
        return tags
    
    