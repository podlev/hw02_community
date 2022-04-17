from django.shortcuts import render, get_object_or_404

from .models import Post, Group

POSTS_COUNT = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:POSTS_COUNT]
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)


def group_post(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_COUNT]
    context = {'posts': posts, 'group': group}
    return render(request, 'posts/group_list.html', context)
