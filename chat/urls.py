from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^chat/$', 'chat.views.chat', name='chat'),
    url(r'^chat_api$', 'chat.views.chat_api', name='chat_api'),
)
