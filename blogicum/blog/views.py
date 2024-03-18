from django.shortcuts import render
from typing import Union


#post_dict = {post['id']: post for post in posts}


def index(request):
   # context = {'all_posts': reversed(posts)}
    return render(request, 'blog/index.html')


def post_detail(request, post_id):
    #context = {'post': post_dict.get(post_id)}
    return render(request, 'blog/detail.html')


def category_posts(request, category_slug):
    context = {'category': category_slug}
    return render(request, 'blog/category.html', context)
