from models import Platform, Game, Genre
from celery import task
import httplib2
import urllib

import logging
logger = logging.getLogger(__name__)

import jsonconvert

try: import simplejson as json
except ImportError: import json

from xml.dom import minidom
from datetime import *

class PlatformCrawler(object):
    @task(ignore_result=True, name="platformList")
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
            
        gamecrawler = GameCrawler(platform_id)
        gamecrawler.crawl.apply_async([gamecrawler])

class GameCrawler(object):
    def __init__(self, platform_id):
        self.platform_id = platform_id
    
    @task(ignore_result=True, name="gameList")    
    def crawl(self):
        try:
            response, content = httplib2.Http().request("http://thegamesdb.net/api/GetPlatformGames.php?platform="+str(self.platform_id), "GET")
            dom = minidom.parseString(content)
            for game in dom.getElementsByTagName('Game'):
                self.processGame.apply_async([self, game.toxml()], queue="game")
        except:
            logger.warn("Error getting games list.")
    
    @task(ignore_result=True, name="gameDetails")
    def processGame(self, game):
        gamedom = minidom.parseString(game)
        try:
            game_id = int(gamedom.getElementsByTagName('id')[0].childNodes[0].nodeValue)
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
        
        if not (game_id and platform_id and title):
            return
        
        release_date = None
        try:
            release_date_str = str(game.getElementsByTagName('ReleaseDate')[0].childNodes[0].nodeValue)
            release_date = datetime.strptime(release_date_str, '%m/%d/%Y').date()
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
        
        baseurl = ""
        try:
            baseurl = game.getElementsByTagName('baseImgUrl')[0].childNodes[0].nodeValue
            #imagedom = game.getElementsByTagName('Images')[0]
            #images = '{"baseurl":"' + baseurl + '", "images":'  + jsonconvert.getjson(imagedom) + '}'
        except:
            pass
        
        ''' For Fan Arts '''
        fanarts_json = ""
        try:
            o_fanarts = []
            t_fanarts = []
            fanartdom = game.getElementsByTagName('fanart')
            for element in fanartdom:
                img_orig = baseurl + element.getElementsByTagName('original')[0].childNodes[0].nodeValue
                img_thumb = baseurl + element.getElementsByTagName('thumb')[0].childNodes[0].nodeValue
                o_fanarts.append(img_orig)
                t_fanarts.append(img_thumb)
                
            o_fanarts_str = '[' + ','.join(['"'+str(item)+'"' for item in o_fanarts]) + ']'
            t_fanarts_str = '[' + ','.join(['"'+str(item)+'"' for item in t_fanarts]) + ']'
            
            fanarts_json = '{"original": ' + o_fanarts_str + ', "thumbnail": ' + t_fanarts_str + '}'
        except:
            pass
        
        ''' For Screen Shots '''
        screenshots_json = ""
        try:
            o_screenshots = []
            t_screenshots = []
            screenshotdom = game.getElementsByTagName('screenshot')
            for element in screenshotdom:
                img_orig = baseurl + element.getElementsByTagName('original')[0].childNodes[0].nodeValue
                img_thumb = baseurl + element.getElementsByTagName('thumb')[0].childNodes[0].nodeValue
                o_screenshots.append(img_orig)
                t_screenshots.append(img_thumb)
                
            o_screenshots_str = '[' + ','.join(['"'+str(item)+'"' for item in o_screenshots]) + ']'
            t_screenshots_str = '[' + ','.join(['"'+str(item)+'"' for item in t_screenshots]) + ']'
            
            screenshots_json = '{"original": ' + o_screenshots_str + ', "thumbnail": ' + t_screenshots_str + '}'
        except:
            pass
        
        ''' For Box Arts '''
        boxarts_json = ""
        try:
            o_boxarts = []
            t_boxarts = []
            type_boxarts = []
            boxartdom = game.getElementsByTagName('boxart')
            for element in boxartdom:
                img_orig = baseurl + element.childNodes[0].nodeValue
                img_thumb = baseurl + element.getAttribute('thumb')
                img_type = element.getAttribute('side')
                o_boxarts.append(img_orig)
                t_boxarts.append(img_thumb)
                type_boxarts.append(img_type)
                
            o_boxarts_str = '[' + ','.join(['"'+str(item)+'"' for item in o_boxarts]) + ']'
            t_boxarts_str = '[' + ','.join(['"'+str(item)+'"' for item in t_boxarts]) + ']'
            type_boxarts_str = '[' + ','.join(['"'+str(item)+'"' for item in type_boxarts]) + ']'
            
            boxarts_json = '{"original": ' + o_boxarts_str + ', "thumbnail": ' + t_boxarts_str + ', "type": ' + type_boxarts_str + '}'
        except:
            pass
        
        ''' For Banners '''
        banners_json = ""
        try:
            o_banners = []
            bannerdom = game.getElementsByTagName('banner')
            for element in bannerdom:
                img_orig = baseurl + element.childNodes[0].nodeValue
                o_banners.append(img_orig)
                
            o_banners_str = '[' + ','.join(['"'+str(item)+'"' for item in o_banners]) + ']'
            banners_json = '{"original": ' + o_banners_str + '}'
        except:
            pass
        
        ''' For ClearLogo '''
        clearlogo = ""
        try:
            clearlogo = baseurl + game.getElementsByTagName('clearlogo')[0].childNodes[0].nodeValue
        except:
            pass
        
        genres = []
        try:
            genredom = game.getElementsByTagName('Genres')[0].getElementsByTagName('genre')
            for genre_element in genredom:
                genreobj, created = Genre.objects.get_or_create(name=str(genre_element.childNodes[0].nodeValue))
                genres.append(genreobj)
        except:
            pass
        
        #print game_id, title, platform_id, release_date, overview, youtube_link, publisher, developer, esrb, players, co_op, rating, fanarts_json, boxarts_json, screenshots_json, banners_json, clearlogo
        
        platformobj = Platform.objects.get(platform_id=platform_id)
        logger.warn("Processing game %s on %s platform"%(title, platformobj.name))
        
        gameobj, created = Game.objects.get_or_create(title=title, platform=platformobj, defaults={'game_id': game_id, 'overview': overview, 'esrb': esrb, 'youtube_link': youtube_link, 'release_date': release_date, 'players': players, 'co_op': co_op, 'publisher': publisher, 'developer': developer, 'rating': rating, 'fanarts': fanarts_json, 'screenshots': screenshots_json, 'boxarts': boxarts_json, 'banners': banners_json, 'clearlogo': clearlogo})
        
        if not created:
            gameobj.game_id = game_id
            gameobj.overview = overview
            gameobj.release_date = release_date
            gameobj.esrb = esrb
            gameobj.co_op = co_op
            gameobj.players = players
            gameobj.youtube_link = youtube_link
            gameobj.developer = developer
            gameobj.publisher = publisher
            gameobj.rating = rating
            gameobj.fanarts = fanarts_json
            gameobj.screenshots = screenshots_json
            gameobj.boxarts = boxarts_json
            gameobj.banners = banners_json
            gameobj.clearlogo = clearlogo
            gameobj.save()
        
        for genre in genres:
            gameobj.genres.add(genre)
            gameobj.save()
