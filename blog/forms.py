from blog.models import BLogComment
from django import forms



class BlogCommentForm(forms.ModelForm):

    class Meta:
        model = BLogComment
        fields = (
            'message',
        )
        widgets = {
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Message',
                'rows' : 7,
                'cols' : 30
            })
        }

