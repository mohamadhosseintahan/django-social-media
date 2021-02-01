from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import AddPostForm
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required


# Create your views here.

def all_post(request):
    posts = Post.objects.all()
    return render(request, 'posts/all_posts.html', {'posts': posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, created__year=year, created__month=month, created__day=day, slug=slug)
    return render(request, 'posts/post_detail.html', {'post': post})


@login_required
def add_post(request, user_id):
    if user_id == request.user.id:

        if request.method == 'POST':
            form = AddPostForm(request.POST or None)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.user = request.user
                new_post.slug = slugify(form.cleaned_data['body'][:30])
                new_post.save()
                messages.success(request, 'Your post submitted', 'success')
                return redirect('account:dashboard', user_id)
        form = AddPostForm()
        return render(request, 'posts/add_posts.html', {'form': form})
    else:
        return redirect('posts:all_post')


@login_required
def delete_post(request, user_id, post_id):
    if request.user.id == user_id:
        Post.objects.get(pk=post_id).delete()
        messages.success(request, 'your post deleted successfully', 'success')
        return redirect('account:dashboard', user_id)
    else:
        return redirect('posts:all_post')
