from django.shortcuts import render, get_object_or_404
from .models import Post


def all_blogs(request):
    posts = Post.objects.order_by('date')
    return render(request, 'blog/all_blogs.html', {'posts': posts})


def blog_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/blog_details.html', {'post': post})
