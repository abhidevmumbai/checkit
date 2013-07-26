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
    url(r'^platforms/$', views.PlatformListView.as_view(), name="platformlist"),
    url(r'^games/$', views.GameListView.as_view(), name="gamelist"),
    url(r'^games/(?P<pk>\d+)/$', views.GameDetailView.as_view(), name="gamedetails"),
    url(r'^manage/$', views.ApiGame.as_view(), name="managelist"),
    url(r'^mygames/$', views.MyGameListView.as_view(), name="mygamelist"),
    url(r'^getcaptcha/$', views.CaptchaGenerate.as_view(), name="captcha"),
    url(r'^facebook/', views.FacebookView.as_view(), name='facebook'),
    url(r'^forgot_password/$', 'forgot_password', name="forgot_password"),
    url(r'^user/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/user/password/reset/done/'}, name="password_reset"),
    url(r'^user/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^privacypolicy/$', TemplateView.as_view(template_name="privacypolicy.html"), name="privacypolicy"),
    url(r'^terms/$', TemplateView.as_view(template_name="terms.html"), name="terms"),
)