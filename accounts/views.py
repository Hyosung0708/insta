from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomProfileForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from .models import User
from django.contrib.auth import get_user_model

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
        
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('posts:index')
        
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)


def profile(request, username):
    User = get_user_model()

    user_info = User.objects.get(username=username)

    context = {
        'user_info': user_info,
    }

    return render(request, 'accounts/profile.html', context)

from django.contrib.auth.decorators import login_required

@login_required
def follow(request, username):
    User = get_user_model()

    me = request.user
    you = User.objects.get(username=username)

    if me in you.followers.all():
        me.followings.remove(you)
    else:
        me.followings.add(you)

    return redirect('accounts:profile', username=username)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')



def search_profile(request):
    
    username = request.GET.get('username')
    print(username)

    try:
        user = get_user_model().objects.get(username=username)
        return redirect('accounts:profile', username=username)
    except:
        return redirect('posts:index')
