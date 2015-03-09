from django.conf.urls import patterns, include, url
from luckymall import views

urlpatterns = patterns('',
    url(r'^$', views.luckymall, name='lucky'),
)
