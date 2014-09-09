from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
  url(r'^$', views.PostsIndex.as_view(), name = 'index')
)
