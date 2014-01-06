from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eforea.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'static_pages.views.index', name='home'),
    url(r'^events$', 'static_pages.views.events', name='events'),
    url(r'^projects$', 'static_pages.views.projects', name='projects'),
    url(r'^startups$', 'static_pages.views.startups', name='startups'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^epitch/', include('epitch.urls', namespace="epitch")),
)
