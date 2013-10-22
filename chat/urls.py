from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^chat/$', 'chat.views.home', name='chat'),
    url(r'^node_api$', 'chat.views.node_api', name='node_api'),
)
