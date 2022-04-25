from .models import Post, Group, User

from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, get_object_or_404


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'posts/index.html', context)


def group_post(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'group': group}
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user = User.objects.get(username=username)
    post_list = Post.objects.filter(author=user)
    posts_count = user.posts.count()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'user': user,
               'posts_count': posts_count,
               'page_obj': page_obj}
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    posts_count = post.author.posts.count()
    title = post.text[:30]
    context = {'title': title,
               'post': post,
               'posts_count': posts_count}
    return render(request, 'posts/post_detail.html', context)
