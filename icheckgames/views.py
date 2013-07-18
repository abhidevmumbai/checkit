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

from models import UserProfile, Game, Genre, Platform, GameMap
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, View, TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from forms import UsersForm, UsersEditForm

from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

from gamesearch.models import GameKeyword, Recommendation
from gamesearch.stemmers import CustomStemmer

from gamesearch.recommender import *

from django.conf import settings
from utils import getAccessToken
import facebook

from django.contrib.auth.views import password_reset
from django.shortcuts import render

class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CSRFExemptMixin, self).dispatch(request, *args, **kwargs)
    
class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class MessageMixin(object):
    def get_context_data(self, **kwargs):
        context = super(MessageMixin, self).get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context

'''
    Method to get Recommended Games for a particular user
'''
def getRecommendedGames(user):
    #Check if the user is present in the Recommendations table
    if Recommendation.objects.filter(user=user):
        recommendedGames = Recommendation.objects.get(user=user).gameslist.all()
        return recommendedGames
    return None

'''
    Method for handling the Forgot password flow
'''
def forgot_password(request):
    if request.method == 'POST':
        return password_reset(request, 
            from_email=request.POST.get('email'))
    else:
        return render(request, 'forgot_password.html')

class CaptchaGenerate(TemplateView):
    def get(self, request, *args, **kwargs):
        json_response = dict()
        json_response['key'] = CaptchaStore.generate_key()
        json_response['image'] = captcha_image_url(json_response['key'])
        return HttpResponse(json.dumps(json_response), content_type='application/json')

'''
    User login view
'''
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

'''
    Facebook login
'''
class FacebookView(View):
    
    def get(self, request, *args, **kwargs):
        try:
            code = request.GET.get("code")

            if not code:
                return HttpResponseRedirect(settings.FACEBOOK_AUTH_URL)
            
            access_token = getAccessToken(code)
            if not access_token:
                return HttpResponseRedirect(reverse_lazy('login'))
            graph = facebook.GraphAPI(access_token)
            profile = graph.get_object("me")
            username = profile['username']
            first_name = profile['first_name']
            last_name = profile['last_name']
            fb_id = profile['id']
            email = profile['email']
            user, created = User.objects.get_or_create(username=username)
            #Getting profile pic and cover pic urls
            extra_fields = graph.get_connections("me", "", fields=["picture.type(large)", "cover"])
            avatar = extra_fields['picture']['data']['url']
            cover = extra_fields['cover']['source']
            print extra_fields
            if created:
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
                user.userprofile.facebookUser = True
                user.userprofile.facebookId = fb_id
                user.userprofile.facebookToken = access_token
                user.userprofile.avatar = avatar
                user.userprofile.cover = cover
            else:
                user.userprofile.facebookToken = access_token
            user.userprofile.save()
            
            user = authenticate(username=username)
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('home'))
        except:
            return HttpResponseRedirect(reverse_lazy('login'))

'''
   User's home view
'''
class HomeView(MessageMixin, LoginRequiredMixin, TemplateView):
    template_name = "home.html"
     
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        return context

    def get(self, request, *args, **kwargs):
        return super(HomeView, self).get(request, *args, **kwargs)

'''
    User registration view
'''
class UserCreate(MessageMixin, FormView):
    template_name = "usercreate.html"
    form_class = UsersForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'You have registered successfully! Please login.')
        return super(UserCreate, self).form_valid(form)

'''
    User profile edit view
'''
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


'''
    Game list view
'''
class GameListView(MessageMixin, ListView):
    paginate_by = 20
    model = Game
    context_object_name = 'games'
    template_name = "gamelist_thumb.html"

    def get_context_data(self, **kwargs):
        genres = Genre.objects.all()
        platforms = Platform.objects.all()
        selected_genre = self.request.GET.get('genre')
        selected_platform = self.request.GET.get('platform')
        search_string = self.request.GET.get('search')
        context = super(GameListView, self).get_context_data(**kwargs)
        if selected_genre:
            context['selected_genre'] = int(selected_genre)

        if selected_platform:
            context['selected_platform'] = int(selected_platform)

        context['genres'] = genres
        context['platforms'] = platforms
        context['search_string'] = search_string
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
                games = genreobj.game_set.filter(platform=platformobj).order_by('title')
            elif genreobj:
                games = genreobj.game_set.all().order_by('title')
            elif platformobj:
                games = platformobj.game_set.all().order_by('title')
            else:
                games = Game.objects.all().order_by('title')
        else:
            games = []
            title_games = []
            other_games = []
            words = []
            words_list = re.compile('[\w]+').findall(search_string)
            
            ''' Stem the word '''
            stemmer = CustomStemmer()
            for element in words_list:
                word = stemmer.stem(element)
                if word:
                    words.append(word)
                    
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
                            title_games = common_title_games + other_uncommon_in_title_games + other_uncommon_in_selected_title_games
                            #title_games = title_games & set(selected_title_games)
                        else:
                            title_games = set(selected_title_games)
                            
                    if selected_other_games:
                        if other_games:
                            '''
                            set_selected_other_games = set(selected_other_games)
                            common_other_games = [x for x in other_games if x in set_selected_other_games]
                            set_common_other_games = set(common_other_games)
                            other_uncommon_in_other_games = [x for x in other_games if x not in set_common_other_games]
                            other_uncommon_in_selected_other_games = [x for x in selected_other_games if x not in set_common_other_games]
                            other_games = common_other_games + other_uncommon_in_other_games + other_uncommon_in_selected_other_games
                            '''
                            other_games = other_games & set(selected_other_games)
                        else:
                            other_games = set(selected_other_games)
                except:
                    pass
            
            games = list(title_games) + list(other_games)
        return games

'''
    Game details view
'''
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

'''
    Api endpoint to add/remove games in the list
'''
class ApiGame(CSRFExemptMixin, LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        success = False
        message = "Insufficient details for processing."
        
        user = request.user
        game_id = request.POST.get("game_id")
        game_task = request.POST.get("game_task")
        game_flag = request.POST.get("game_flag")

        if game_flag == "true":
            game_flag = True
        else:
            game_flag = False

        if not (game_id and game_task):
            content = json.dumps({"success": success, "message": message})
            return HttpResponse(content, content_type='application/json')
        
        game_id = int(game_id)
        game_task = int(game_task)
        if game_task == 1:
            #Add mapping
            try:
                game = Game.objects.get(id=game_id)
                gamemap, created = GameMap.objects.get_or_create(user=user, game=game)
                if created:
                    message = "Game added to your list."
                else:
                    message = "Game already in your list."
                success = True
                recommender = Recommender()
                recommender.build.apply_async([recommender, user], queue="recommender");
            except:
                message = "Error creating game in list."
        elif game_task == 2:
            #Delete mapping
            try:
                game = Game.objects.get(id=game_id)
                gamemap = GameMap.objects.get(user=user, game=game)
                gamemap.delete()
                message = "Game removed from your list."
                success = True
                recommender = Recommender()
                recommender.build.apply_async([recommender, user], queue="recommender");
            except:
                message = "Error while deleting game in list."
        elif game_task == 3:
            #Mark Owned
            game = Game.objects.get(id=game_id)
            gamemap = GameMap.objects.get(user=user, game=game)
            gamemap.owned = game_flag
            gamemap.save()
            message = "Game marked as owned."
            success = True
        elif game_task == 4:
            #Mark Completed
            game = Game.objects.get(id=game_id)
            gamemap = GameMap.objects.get(user=user, game=game)
            gamemap.status = 'completed'
            gamemap.save()
            message = "Game marked as completed."
            success = True
        elif game_task == 5:
            #Mark as currently playing
            game = Game.objects.get(id=game_id)
            gamemap = GameMap.objects.get(user=user, game=game)
            gamemap.status = 'current'
            gamemap.save()
            message = "Game added in current list."
            success = True
        elif game_task == 6:
            #Mark as On hold
            game = Game.objects.get(id=game_id)
            gamemap = GameMap.objects.get(user=user, game=game)
            gamemap.status = 'onhold'
            gamemap.save()
            message = "Game on hold."
            success = True
        elif game_task == 7:
            #Mark Favorite
            game = Game.objects.get(id=game_id)
            gamemap = GameMap.objects.get(user=user, game=game)
            gamemap.favorite = game_flag
            gamemap.save()
            message = "Game marked as favorite."
            success = True
        elif game_task == 8:
            #Mark Wish
            game = Game.objects.get(id=game_id)
            gamemap = GameMap.objects.get(user=user, game=game)
            gamemap.wish = game_flag
            gamemap.save()
            message = "Game added in wishlist."
            success = True            
        elif game_task == 9:
            #Mark as Dropped playing
            game = Game.objects.get(id=game_id)
            gamemap = GameMap.objects.get(user=user, game=game)
            gamemap.status = 'dropped'
            gamemap.save()
            message = "Game dropped."
            success = True
        elif game_task == 10:
            #Mark as Not started
            game = Game.objects.get(id=game_id)
            gamemap = GameMap.objects.get(user=user, game=game)
            gamemap.status = 'notstarted'
            gamemap.save()
            message = "Game not started yet."
            success = True

        else:
            message = "Invalid task."
        content = json.dumps({"success": success, "message": message})
        return HttpResponse(content, content_type='application/json')

    def get(self, request, *args, **kwargs):
        return HttpResponse("No data available.")

'''
    Logged in User's games list
'''
class MyGameListView(LoginRequiredMixin, MessageMixin, ListView):
    paginate_by = 20
    model = GameMap
    context_object_name = 'gamelinks'
    template_name = "mygamelist.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(MyGameListView, self).get_context_data(**kwargs)        
        context['recommendedGames'] = getRecommendedGames(user)
        return context

    def get_queryset(self):
        user = self.request.user
        tag = self.request.GET.get('tag')
        try:
            if tag=='current' or tag=='completed' or tag=='onhold' or tag== 'dropped' or tag== 'notstarted':
                gamelinks = user.gamemap_set.filter(status=tag)
            else:
                gamelinks = user.gamemap_set.filter(**{tag:True})
        except:
            gamelinks = user.gamemap_set.all()
        return gamelinks

'''
    Platform list
'''
class PlatformListView(MessageMixin, ListView):
    paginate_by = 15
    model = Platform
    context_object_name = 'platforms'
    template_name = "platformlist.html"

    def get_context_data(self, **kwargs):
        context = super(PlatformListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        platformlist = Platform.objects.all()
        return platformlist
