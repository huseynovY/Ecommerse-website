from product.models import ProductComment
from django import forms



class ProductCommentForm(forms.ModelForm):

    class Meta:
        model = ProductComment
        fields = (
            'message',
        )
        widgets = {
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Write your review',
                'rows' : 7,
                'cols' : 30
            })
        }

