from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from icheckgames import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="landing.html"), name='splash'),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    url(r'^usercreate/$', views.UserCreate.as_view(), name="usercreate"),
    url(r'^useredit/$', views.UserEdit.as_view(), name="useredit"),
    url(r'^games/$', views.GameListView.as_view(), name="gamelist"),
)