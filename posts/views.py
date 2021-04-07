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
    form = PostForm(request.POST or None)
    if not form.is_valid():
        return render(request, "new_post.html", {'form': form})
    post = form.save(commit=False)
    post.author = request.user
    post.save()
    return redirect('index')
