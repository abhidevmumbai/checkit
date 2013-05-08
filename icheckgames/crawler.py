from models import Platform, Game, Genre
import httplib2
import urllib

import logging
logger = logging.getLogger(__name__)

try: import simplejson as json
except ImportError: import json

from xml.dom import minidom

class PlatformCrawler(object):
    def crawl(self):
        try:
            response, content = httplib2.Http().request("http://thegamesdb.net/api/GetPlatformsList.php", "GET")
            dom = minidom.parseString(content)
            for platform in dom.getElementsByTagName('Platform'):
                self.processPlatform(platform)
        except:
            logger.warn("Error getting platforms list.")
    
    def processPlatform(self, platform):
        platform_id = None
        name = None
        alias = ""
        try:
            platform_id = int(platform.getElementsByTagName('id')[0].childNodes[0].nodeValue)
            name = str(platform.getElementsByTagName('name')[0].childNodes[0].nodeValue)
            alias = str(platform.getElementsByTagName('alias')[0].childNodes[0].nodeValue)
        except:
            logger.warn("Some error parsing platform.")
        
        if platform_id and name:
            platformobj, created = Platform.objects.get_or_create(name=name, defaults={'platform_id': platform_id, 'alias': alias})
            
            if not created:
                platformobj.platform_id = platform_id
                platformobj.alias = alias
                platformobj.save()

class GameCrawler(object):
    def crawl(self, platform_id):
        try:
            response, content = httplib2.Http().request("http://thegamesdb.net/api/GetPlatformGames.php?platform="+str(platform_id), "GET")
            dom = minidom.parseString(content)
            for game in dom.getElementsByTagName('Game'):
                self.processGame(game)
        except:
            logger.warn("Error getting platforms list.")
    
    def processGame(self, game):
        try:
            game_id = int(game.getElementsByTagName('id')[0].childNodes[0].nodeValue)
            response, content = httplib2.Http().request("http://thegamesdb.net/api/GetGame.php?id="+str(game_id), "GET")
            dom = minidom.parseString(content)
            self.processGameDetails(dom)
        except:
            logger.warn("Some error getting game details.")

    def processGameDetails(self, game):
        game_id = None
        try:
            game_id = int(game.getElementsByTagName('id')[0].childNodes[0].nodeValue)
        except:
            pass
        
        title = None
        try:
            title = str(game.getElementsByTagName('GameTitle')[0].childNodes[0].nodeValue)
        except:
            pass
        
        platform_id = None
        try:
            platform_id = int(game.getElementsByTagName('PlatformId')[0].childNodes[0].nodeValue)
        except:
            pass
        
        release_date = None
        try:
            release_date = str(game.getElementsByTagName('ReleaseDate')[0].childNodes[0].nodeValue)
        except:
            pass
        
        overview = ""
        try:
            overview = str(game.getElementsByTagName('Overview')[0].childNodes[0].nodeValue)
        except:
            pass
        
        youtube_link = ""
        try:
            youtube_link = str(game.getElementsByTagName('Youtube')[0].childNodes[0].nodeValue)
        except:
            pass
        
        publisher = ""
        try:
            publisher = str(game.getElementsByTagName('Publisher')[0].childNodes[0].nodeValue)
        except:
            pass
        
        developer = ""
        try:
            developer = str(game.getElementsByTagName('Developer')[0].childNodes[0].nodeValue)
        except:
            pass
        
        esrb = ""
        try:
            esrb = str(game.getElementsByTagName('ESRB')[0].childNodes[0].nodeValue)
        except:
            pass
            
        players = 1
        try:
            players = int(game.getElementsByTagName('Players')[0].childNodes[0].nodeValue)
        except:
            pass
        
        co_op = False
        try:
            str_co_op = str(game.getElementsByTagName('Co-op')[0].childNodes[0].nodeValue)
            if str_co_op == "Yes":
                co_op = True
        except:
            pass
        
        rating = float(0)
        try:
            rating = float(game.getElementsByTagName('Rating')[0].childNodes[0].nodeValue)
        except:
            pass
        
        #print game_id, title, platform_id, release_date, overview, youtube_link, publisher, developer, esrb, players, co_op, rating
        
        if game_id and platform_id and title:
            platformobj = Platform.objects.get(platform_id=platform_id)
            gameobj, created = Game.objects.get_or_create(title=title, defaults={'game_id': game_id, 'overview': overview, 'esrb': esrb, 'players': players, 'co_op': co_op, 'publisher': publisher, 'developer': developer, 'rating': rating})
            
            if not created:
                gameobj.game_id = game_id
                gameobj.overview = overview
                gameobj.esrb = esrb
                gameobj.co_op = co_op
                gameobj.players = players
                gameobj.developer = developer
                gameobj.publisher = publisher
                gameobj.rating = rating
                gameobj.save()
            
            gameobj.platforms.add(platformobj)
            gameobj.save()
