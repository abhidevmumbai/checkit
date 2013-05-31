# Create your views here.
import logging
logger = logging.getLogger(__name__)

import re

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

from models import Game, Genre, Platform
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, View, TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from forms import UsersForm, UsersEditForm

from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

from gamesearch.models import GameKeyword

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
        context['user'] = user
        return context

    def get(self, request, *args, **kwargs):
        return super(HomeView, self).get(request, *args, **kwargs)

class UserCreate(MessageMixin, FormView):
    template_name = "usercreate.html"
    form_class = UsersForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'You have registered successfully! Please login.')
        return super(UserCreate, self).form_valid(form)

class UserEdit(LoginRequiredMixin, MessageMixin, FormView):
    form_class = UsersEditForm
    success_url = reverse_lazy('home')
    template_name = "useredit.html"
    
    def get_context_data(self, **kwargs):
        context = super(UserEdit, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context

    def get_form_kwargs(self):
        kwargs = super(UserEdit, self).get_form_kwargs()
        user = self.request.user
        self.user = user
        kwargs['user'] = user
        return kwargs
    
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Profile updated successfully.')
        return super(UserEdit, self).form_valid(form)

class GameListView(MessageMixin, ListView):
    paginate_by = 20
    model = Game
    context_object_name = 'games'
    template_name = "gamelist.html"

    def get_context_data(self, **kwargs):
        genres = Genre.objects.all()
        platforms = Platform.objects.all()
        selected_genre = self.request.GET.get('genre')
        selected_platform = self.request.GET.get('platform')

        context = super(GameListView, self).get_context_data(**kwargs)
        if selected_genre:
            context['selected_genre'] = int(selected_genre)

        if selected_platform:
            context['selected_platform'] = int(selected_platform)

        context['genres'] = genres
        context['platforms'] = platforms
        return context

    def get_queryset(self):
        selected_genre = self.request.GET.get('genre')
        selected_platform = self.request.GET.get('platform')
        search_string = self.request.GET.get('search')
        
        try:
            genreobj = Genre.objects.get(id=selected_genre)
        except:
            genreobj = None
        
        try:
            platformobj = Platform.objects.get(id=selected_platform)
        except:
            platformobj = None
        
        if not search_string:
            if genreobj and platformobj:
                games = genreobj.game_set.filter(platform=platformobj)
            elif genreobj:
                games = genreobj.game_set.all()
            elif platformobj:
                games = platformobj.game_set.all()
            else:
                games = Game.objects.all()
        else:
            games = []
            title_games = []
            other_games = []
            words_list = re.compile('[\w]+').findall(search_string)
            words = [element.lower() for element in words_list]
            for word in words:
                try:
                    keywordobj = GameKeyword.objects.get(word=word)
                    
                    if genreobj and platformobj:
                        selected_title_games = keywordobj.title_games.filter(platform=platformobj).filter(genres__id=selected_genre)
                        selected_other_games = keywordobj.other_games.filter(platform=platformobj).filter(genres__id=selected_genre)
                    elif genreobj:
                        selected_title_games = keywordobj.title_games.filter(genres__id=selected_genre)
                        selected_other_games = keywordobj.other_games.filter(genres__id=selected_genre)
                    elif platformobj:
                        selected_title_games = keywordobj.title_games.filter(platform=platformobj)
                        selected_other_games = keywordobj.other_games.filter(platform=platformobj)
                    else:
                        selected_title_games = keywordobj.title_games.all()
                        selected_other_games = keywordobj.other_games.all()
                    
                    if selected_title_games:
                        if title_games:
                            set_selected_title_games = set(selected_title_games)
                            common_title_games = [x for x in title_games if x in set_selected_title_games]
                            set_common_title_games = set(common_title_games)
                            other_uncommon_in_title_games = [x for x in title_games if x not in set_common_title_games]
                            other_uncommon_in_selected_title_games = [x for x in selected_title_games if x not in set_common_title_games]
                            title_games = common_title_games
                            title_games.extend(other_uncommon_in_title_games)
                            title_games.extend(other_uncommon_in_selected_title_games)
                        else:
                            title_games = selected_title_games
                            
                    if selected_other_games:
                        if other_games:
                            other_games = list(set(other_games) & set(selected_other_games)) + list(set(other_games) ^ set(selected_other_games))
                        else:
                            other_games = selected_other_games
                except:
                    pass
            
            games = title_games# + list(other_games)
        
        '''
        #Filter results according to genre and/or platform

        if ((selected_genre and int(selected_genre) != 0) and (not selected_platform or int(selected_platform)==0)):
            print 'Only genre id'
            games = Game.objects.filter(genres__id=selected_genre).order_by('title')
        elif ((selected_platform and int(selected_platform) != 0) and (not selected_genre or int(selected_genre)==0)):
            print 'Only platform id'
            games = Game.objects.filter(platform_id=selected_platform).order_by('title')
        elif ((selected_genre and int(selected_genre) != 0) and (selected_platform and int(selected_platform) != 0)):
            print 'Both genre and platform id'
            games = Game.objects.filter(genres__id=selected_genre)
            games = games.filter(platform_id=selected_platform).order_by('title')
        else:
            print 'Get all games'
            games = Game.objects.all().order_by('title')
        '''
        return games

class GameDetailView(MessageMixin, DetailView):
    model = Game
    context_object_name = 'game'
    template_name = "gamedetails.html"

    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)
        game = self.object
        screenshots = json.loads(game.screenshots)
        fanarts = json.loads(game.fanarts)
        try:
            context['screenshots'] = screenshots
            context['fanarts'] = fanarts
            
            youtube_vcode = game.youtube_link.split('=')[1]
            context['youtube_vcode'] = youtube_vcode
        except:
            pass
        return context