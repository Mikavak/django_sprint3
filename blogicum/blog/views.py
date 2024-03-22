from django.shortcuts import get_object_or_404, render
from datetime import date
from .models import Post, Category
from . import constant as c


def post_filter(**kwargs):
    return Post.objects.filter(
        pub_date__lt=date.today(),
        is_published=True,
        category__is_published=True, **kwargs)


def index(request):
    post = post_filter()[:c.CONSTANT]
    context = {'post_list': post}
    return render(request, 'blog/index.html', context)


def category_posts(request, category_slug):
    posts_of_category = get_object_or_404(
        Category.objects.values('title', 'description').filter(
            is_published=True), slug=category_slug)
    """В этом кверисете не стал делать через вызов
    функции т.к. отсутсвует в условие фильтра
    category__is_published=True"""
    post_list = Post.objects.filter(
        pub_date__lt=date.today(),
        category__slug=category_slug,
        is_published=True)
    context = {'category': posts_of_category,
               'post_list': post_list}
    return render(request, 'blog/category.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(post_filter(pk=post_id))
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
