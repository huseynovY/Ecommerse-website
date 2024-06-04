from modeltranslation.translator import translator, TranslationOptions
from blog.models import Blogcategory, Blogtag

class BLogcategoryTranslationOption(TranslationOptions):
    fields = ('title', )

translator.register(Blogcategory, BLogcategoryTranslationOption)

class BlogtagTranslationOptions(TranslationOptions):
    fields = ('title', )

translator.register(Blogtag, BlogtagTranslationOptions)