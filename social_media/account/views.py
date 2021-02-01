from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post

from .forms import UserLoginForm, UserRegistrationForm


# Create your views here.
def user_login(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                if next:
                    return redirect(next)

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


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'you logged out successfully', 'success')
    return redirect('posts:all_post')


@login_required
def dashboard(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(user=user)
    self_dash = False
    if user_id ==request.user.id:
        self_dash = True
    return render(request, 'account/dashboard.html', {'user': user,
                                                      'posts': posts,
                                                      'self_dash' : self_dash})
