from modeltranslation.translator import translator, TranslationOptions
from product.models import Category , Tag, Color

class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Category, CategoryTranslationOptions)

class TagTranslationOption(TranslationOptions):
    fields = ('title', )

translator.register(Tag, TagTranslationOption)

class ColorTranslationOption(TranslationOptions):
    fields = ('title', )

translator.register(Color,ColorTranslationOption )