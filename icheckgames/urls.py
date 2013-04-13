from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from icheckgames import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="landing.html"), name='splash'),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    url(r'^usercreate/$', views.UserCreate.as_view(), name="usercreate"),
    #url(r'^useredit/$', views.UserEdit.as_view(), name="useredit"),
    #url(r'^apps/$', views.AppView.as_view(), name="applist"),
    #url(r'^apps/create$', views.AppCreate.as_view(), name="appcreate"),
    #url(r'^apps/(?P<pk>\d+)/edit$', views.AppEdit.as_view(), name="appedit"),
    #url(r'^apps/(?P<pk>\d+)/delete$', views.AppDelete.as_view(), name="appdelete"),
    #url(r'^getcaptcha/$', views.CaptchaGenerate.as_view(), name="captcha"),
    #url(r'^generate_secret_key/$', views.SecretKeyGenerate.as_view(), name="secretkeygenerate"),
    #url(r'^doc/jsapidoc/$', TemplateView.as_view(template_name="js_api_doc.html"), name="jsapidoc"),
    #url(r'^doc/apigatewaydoc/$', TemplateView.as_view(template_name="api_gateway_doc.html"), name="apigatewaydoc")
)