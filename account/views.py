from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from account.tokens import account_activation_token

from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from product.models import Product


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        django_login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


def loginregister(request):
    form = RegisterForm()
    loginform = LoginForm()
    if request.method == 'POST':

        if "register" in request.POST:
         
                
         form = RegisterForm(data= request.POST)
         
         if form.is_valid():
            user = form.save(False) 
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect(reverse_lazy('home'))
        else:
            loginform = LoginForm(data= request.POST)
            
            if loginform.is_valid():  
                next = request.GET.get('next', reverse_lazy('home'))
                user = authenticate(
                    request= request,
                    username = loginform.cleaned_data['username'],
                    password = loginform.cleaned_data['password'],
                )
                if not user:
                    messages.add_message(request, messages.ERROR, 'User not found!')
                else:
                    django_login(request, user)
                    return redirect(next)
    context = {
        'form' : form,
        'loginform' : loginform
    }
    return render(request, 'login-register.html', context)
def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('login-register'))



@login_required(login_url =('login-register'))
def profile(request):
    user = request.user
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            new_image = form.cleaned_data['image']
            old_password = form.cleaned_data['password']
            new_password = form.cleaned_data['new_password']

            if not check_password(old_password, user.password):
                messages.error(request, 'Incorrect current password.')
            elif old_password == new_password:
                messages.error(request, 'New password must be different from the current password.')
            else:
                if new_image:
                    user.set_image[new_image]
                    user.profile.save()

                
                user.set_password(new_password)
                user.save() 

                messages.success(request, 'Password changed successfully!')
                return redirect(reverse_lazy('profile'))

    context = {
        'form': form,
    }
    return render(request, 'profile.html', context)