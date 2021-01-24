from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('posts:all_post')
            else:
                messages.error(request, 'wrong user name or password')
    else:
        form = UserLoginForm()

    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            login(request, user)
            messages.success(request, 'you registered successfully', 'success')
            return redirect('posts:all_post')
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'you logged out successfully', 'success')
    return redirect('posts:all_post')


def dashboard(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'account/dashboard.html', {'user': user})
