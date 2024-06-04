from typing import Any
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Confirm Password'
    }))

    
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        )
        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'First name'
            }),
            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Last name'
            }),
            'username' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Username'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Email'
            }),
            'password' : forms.PasswordInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Password'
            })  
            
        }

    def save(self, commit: bool = ...) -> Any:

        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        user.save()
        return user
    def clean(self) -> dict[str, Any]:
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Passwords must be same!')
        return super().clean()

class LoginForm(forms.Form):

    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Username'
    }))

    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Password'
    }))
    

class ProfileForm(forms.Form):

    password = forms.CharField(
        max_length=40,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Current Password'
        })
    )
    new_password = forms.CharField(
        max_length=40,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New Password'
        })
    )

    image = forms.ImageField(label='Profile image', required=False)

    def save(self, commit: bool = ...) -> Any:

        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.set_image(self.cleaned_data['image'])
        user.is_active = False
        user.save()
        return user

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     new_password = cleaned_data.get('new_password')

    #     if password == new_password:
    #         raise forms.ValidationError('Passwords must be different!')
    #     return cleaned_data
