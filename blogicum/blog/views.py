from datetime import datetime
from django.shortcuts import get_object_or_404, render

from .constant import CONSTANT_COUNT_OF_POSTS
from .models import Post, Category


def post_filter(**kwargs):
    return Post.objects.filter(
        pub_date__lt=datetime.today(),
        is_published=True,
        category__is_published=True, **kwargs)


def index(request):
    posts = post_filter()[:CONSTANT_COUNT_OF_POSTS]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def category_posts(request, category_slug):
    posts_of_category = get_object_or_404(
        Category.objects.values('title', 'description').filter(
            is_published=True), slug=category_slug)
    posts_list = post_filter(category__slug=category_slug)
    context = {'category': posts_of_category,
               'post_list': posts_list}
    return render(request, 'blog/category.html', context)


def post_detail(request, post_id):
    posts = get_object_or_404(post_filter(pk=post_id))
    context = {'post': posts}
    return render(request, 'blog/detail.html', context)
