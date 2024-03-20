from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from datetime import date
from .models import Post, Category


# post_dict = {post['id']: post for post in posts}


def index(request):
    post = Post.objects.filter(
        pub_date__lte=date.today(),
        is_published=True,
        category__is_published=True).order_by('-pub_date')[:5]
    context = {'post_list': post}
    return render(request, 'blog/index.html', context)


def category_posts(request, category_slug):
    posts_of_category = get_object_or_404(
        Category.objects.values('title', 'description').filter(is_published=True), slug=category_slug)
    post_list = Post.objects.filter(
        pub_date__lt=date.today(),
        category__slug=category_slug,
        is_published=True)
    context = {'category': posts_of_category,
               'post_list': post_list}
    return render(request, 'blog/category.html', context)

    # posts_of_category = get_object_or_404(
    #      Category.objects.values('title', 'description')
    #      .filter(is_published=True), slug=category_slug)
    #  post_list = Post.objects.filter(
    #      category__slug=category_slug)
    #  context = {'category': posts_of_category,
    #             'post_list': post_list}


def post_detail(request, post_id):
    post = get_object_or_404(Post.objects.filter(category__is_published=True, is_published=True, pk=post_id, pub_date__lt=date.today()))
                             
    context = {'post': post}
    return render(request, 'blog/detail.html', context) 
