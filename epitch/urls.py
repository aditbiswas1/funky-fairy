from django.conf.urls import patterns, url

from epitch import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^submit/$', views.submit, name='submit'),
	)