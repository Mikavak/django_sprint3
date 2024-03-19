from django.shortcuts import get_object_or_404, get_list_or_404, render
from datetime import datetime
from .models import Post, Category

# post_dict = {post['id']: post for post in posts}


def index(request):
    post = Post.objects.filter(
        pub_date=datetime.today(),
        is_published=True,
        category__is_published=True).order_by('-pub_date')[:5]
    context = {'post_list': post}
    return render(request, 'blog/index.html', context)


def category_posts(request, category_slug):
    posts_of_category = get_object_or_404(
        Category.objects.values('title', 'description')
        .filter(is_published=True), slug=category_slug)
    post_list = Post.objects.filter(
        category__slug=category_slug)
    context = {'category': posts_of_category,
               'post_list': post_list}
    return render(request, 'blog/category.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post.objects.filter(
        pk=post_id), pub_date__gte=datetime.today, is_published=False, category__is_published=False)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
