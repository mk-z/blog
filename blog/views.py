from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog
from datetime import datetime
from django.http import Http404

# Create your views here.
def home(request):
    post_list = Blog.objects.all()
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request, id):
    try:
        post = Blog.objects.get(id = str(id))
    except Blog.DoesNotExist:
        raise Http404
    return  render(request, 'post.html', {'post':post})

def archives(request):
    try:
        post_list = Blog.objects.all()
    except Blog.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list':post_list, 'error':False})

def about_me(request):
    return render(request, 'aboutme.html')

def search_tag(request, tag):
    try:
        post_list = Blog.objects.filter(category__iexact=tag)
    except Blog.DoesNotExist:
        raise  Http404
    return render(request, 'tag.html', {'post_list':post_list})
