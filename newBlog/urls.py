from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import RssFeed

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^(?P<id>\d+)/$', 'blog.views.detail', name='detail'),
    url(r'archives/$', 'blog.views.archives', name='archives'),
    url(r'about/$', 'blog.views.about_me', name='about'),
    url(r'^tag(?P<tag>\w+)/$', 'blog.views.search_tag', name='search_tag'),
    url(r'^search/$', 'blog.views.blog_search', name='search'),
    url(r'^feed/$', RssFeed(), name='RSS'),
)
