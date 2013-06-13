from django.contrib.auth.models import User
from icheckgames.models import Game, Platform, Genre
from gamesearch.stemmers import CustomStemmer
from gamesearch.models import Recommendation

from celery import task
from django.core.cache import cache

import re

class Recommender(object):
    @task(ignore_result=True, name="Recommender")
    def build(self, user):
        tasks = cache.get("recommender_%s"%(user.username))
        if tasks:
            return
        
        cache.set("recommender_%s"%(user.username), 1, 3600*24)
        
        gamelinks = user.gamemap_set.all()
        positive_sample_games = []
        for link in gamelinks:
            positive_sample_games.append(link.game)
        
        platform_dict = dict()
        total_platforms = 0
        genre_dict = dict()
        total_genres = 0
        all_words = []
        for game in positive_sample_games:
            try:
                platform_count = platform_dict[game.platform.id]
                platform_dict[game.platform.id] = platform_count + 1
            except:
                platform_dict[game.platform.id] = 1
            total_platforms = total_platforms + 1
            
            for genre in game.genres.all():
                try:
                    genre_count = genre_dict[genre.id]
                    genre_dict[genre.id] = genre_count + 1
                except:
                    genre_dict[genre.id] = 1
                total_genres = total_genres + 1
            
            game_words = self.getTitleWords(game)
            set_game_words = set(game_words)
            common_game_words = [x for x in all_words if x in set_game_words]
            set_common_game_words = set(common_game_words)
            other_uncommon_in_all_words = [x for x in all_words if x not in set_common_game_words]
            other_uncommon_in_game_words = [x for x in set_game_words if x not in set_common_game_words]
            all_words = common_game_words + other_uncommon_in_all_words + other_uncommon_in_game_words
            all_words = all_words[0:50]
            
        for (key, value) in platform_dict.iteritems():
            platform_dict[key] = float(value) / float(total_platforms)
        
        for (key, value) in genre_dict.iteritems():
            genre_dict[key] = float(value) /  float(total_genres)
        
        reco_games = []
        set_positive_sample_games = set(positive_sample_games)
        for game in Game.objects.all():
            if game not in set_positive_sample_games:
                game_rank = self.calculateRank(game, platform_dict, genre_dict, all_words)
                reco_games.append([game_rank, game])
                reco_games.sort(key=lambda x: x[0], reverse=True)
                if len(reco_games) > 15:
                    reco_games.pop()
        
        gamerecom, created = Recommendation.objects.get_or_create(user=user)
        
        gamerecom.gameslist.clear()
        for game in reco_games:
            gamerecom.gameslist.add(game[1])
            print (game[1].title).encode('ascii', 'ignore') + "\t" + str(game[0])
        
        cache.set("recommender_%s"%(user.username), 0, 3600*24)
        
    def getTitleWords(self, game):
        stemmer = CustomStemmer()
        title_words_list = re.compile('[\w]+').findall(game.title)
        title_words = []
        for element in title_words_list:
                t_word = stemmer.stem(element)
                if t_word:
                    title_words.append(t_word)
        return title_words
    
    def calculateRank(self, game, platform_ps, genre_ps, title_ws):
        try:
            platform_fraction = platform_ps[game.platform.id]
        except:
            platform_fraction = 0
        
        genre_fraction = float(0)
        genre_count = 0
        for genre in game.genres.all():
            try:
                genre_fraction = genre_fraction + genre_ps[genre.id]
                genre_count = genre_count + 1
            except:
                pass
        
        if not (genre_count == 0):
            genre_fraction = genre_fraction / genre_count
        
        try:
            game_words = self.getTitleWords(game)
            common_words_count = len(set(game_words) & set(title_ws))
            title_fraction = (float(common_words_count)/len(title_ws))**(0.5)
        except:
            title_fraction = 0
            
        game_rank = 0.4 * title_fraction + 0.3 * platform_fraction + 0.3 * genre_fraction
        return game_rank
