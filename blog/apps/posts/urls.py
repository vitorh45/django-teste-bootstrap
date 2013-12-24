from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'posts.views.list', name='post_list'),
    url(r'^(?P<slug>[\w_-]+)/$', 'posts.views.detail', name='post_detail'),    
)