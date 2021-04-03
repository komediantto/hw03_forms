from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Group, Post
from .forms import PostForm


def index(request):
    latest = Post.objects.all()[:11]
    return render(request, 'index.html', {'posts': latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, 'group.html', {'group': group, 'posts': posts})


@login_required
def new_post(request):
    if request.method != 'POST':
        form = PostForm()
        return render(request, 'new_post.html', {'form': form})
    form = PostForm(request.POST)
    if form.is_valid() is False:
        return render(request, 'new_post.html', {'form': form})
    new_item = form.save(commit=False)
    new_item.author = request.user
    new_item.save()
    return redirect('index')
