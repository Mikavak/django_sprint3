from django.shortcuts import render
from typing import Union
from .models import Post

# post_dict = {post['id']: post for post in posts}


def index(request):
    #     дата публикации — не позже текущего времени,
    # значение поля is_published равно True,
    # у категории, к которой принадлежит публикация, значение поля is_published равно True.
    post = Post.objects.filter(is_published=True, category__is_published=True)\
        .order_by('-pub_date')[:5]
    context = {'post_list': post}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    # context = {'post': post_dict.get(post_id)}
    return render(request, 'blog/detail.html')


def category_posts(request, category_slug):
    context = {'category': category_slug}
    return render(request, 'blog/category.html', context)
