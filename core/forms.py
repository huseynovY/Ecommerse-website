from core.models import Contact
from django import forms
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message',
        )
        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Your name')
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Your Email')
            }),
            'subject' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Subject')
            }),
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : _('Message'),
                'rows' : 7,
                'cols' : 30
            })
        }