from django.shortcuts import render
# from django.http import HttpResponse
from blog.models import Blog
# from datetime import datetime
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    posts = Blog.objects.all()
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Blog.objects.get(id=str(id))
    except Blog.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def archives(request):
    try:
        post_list = Blog.objects.all()
    except Blog.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list, 'error': False})


def about_me(request):
    return render(request, 'about.html')


def search_tag(request, tag):
    try:
        post_list = Blog.objects.filter(category__iexact=tag)
    except Blog.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Blog.objects.filter(title__contains=s)
            if len(post_list) == 0:
                return render(request, 'archives.html', {'post_list': post_list, 'error': True})
            else:
                return render(request, 'archives.html', {'post_list': post_list, 'error': False})

    return redirect('/')


class RssFeed(Feed):
    title = "Rss feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Blog.objects.order_by('-date_time1')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time1

    def item_description(self, item):
        return item.content
