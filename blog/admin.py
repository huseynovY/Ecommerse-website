from django.contrib import admin
from blog.models import Blog , Blogcategory, Blogtag, BLogComment
from modeltranslation.admin import TranslationAdmin
from django import forms
# Register your models here.



admin.site.register(BLogComment)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title']
    actions = ['blog_activated', 'blog_deactivated']

    def blog_activated(self, request, queryset):
        queryset.update(status = True)

    def blog_deactivated(self, request, queryset):
        queryset.update(status = False)


@admin.register(Blogcategory)
class BlogcategoryAdmin(TranslationAdmin):
    fields = 'title',


@admin.register(Blogtag)
class BlogtagAdmin(TranslationAdmin):
    fields = 'title',


class BlogAdminForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'blogtags' : forms.CheckboxSelectMultiple, 
        }
