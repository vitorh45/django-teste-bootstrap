from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.index', name='index'),
    url(r'^contato/', 'contact.views.contact', name='contact'),
    url(r'^blog/', include('posts.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^busca/$', 'core.views.search', name='search'),
    #url(r'^grappelli', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

