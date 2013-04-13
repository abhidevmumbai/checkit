# Create your views here.
import logging
logger = logging.getLogger(__name__)

try: import simplejson as json
except ImportError: import json

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.shortcuts import render_to_response

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, View, TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from models import Users
from forms import UsersForm

from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class MessageMixin(object):
    def get_context_data(self, **kwargs):
        context = super(MessageMixin, self).get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context

class LoginView(MessageMixin, FormView):
    template_name = "auth.html"
    form_class = AuthenticationForm
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        #messages.add_message(self.request, messages.SUCCESS, 'You are now logged in successfully')
        return super(LoginView, self).form_valid(form)
    
    def get_success_url(self):
        return self.request.GET.get('next',reverse_lazy('home'))

class LogoutView(TemplateView):
    template_name = "logout.html"
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

class HomeView(MessageMixin, LoginRequiredMixin, TemplateView):
    template_name = "home.html"
     
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        user = self.request.user
        developer = None
        try:
            developer = Users.objects.get(user=user)
        except:
            logger.warn('No developer for given user.')
        context['user'] = user
        return context

class UserCreate(MessageMixin, FormView):
    template_name = "usercreate.html"
    form_class = UsersForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'You have registered successfully! Please login.')
        return super(UserCreate, self).form_valid(form)
