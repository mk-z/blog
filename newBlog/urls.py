from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^(?P<id>\d+)/$', 'blog.views.detail', name='detail'),
    url(r'archives/$', 'blog.views.archives', name='archives'),
    url(r'aboutme/$', 'blog.views.about_me', name='about_me'),
    url(r'^tag(?P<tag>\w+)/$', 'blog.views.search_tag', name='search_tag')
)
