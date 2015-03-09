from django.conf.urls import patterns, include, url
from moneymany import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^joinnow/$', views.joinnow, name='joinnow'),
    url(r'^computer/$', views.computer, name='computer'),
    url(r'^result/$', views.result, name='result'),
    url(r'^message/create', views.create_post, name='create_post'),
    # url(r'^luckymall', views.luckymall, name='luckymall'),
)
