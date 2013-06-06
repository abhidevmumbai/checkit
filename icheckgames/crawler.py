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

from django.utils.encoding import smart_str

class PlatformCrawler(object):
    @task(ignore_result=True, name="platformList")
    def crawl(self):
        try:
            response, content = httplib2.Http().request("http://thegamesdb.net/api/GetPlatformsList.php", "GET")
            content = smart_str(content)
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
            name = unicode(platform.getElementsByTagName('name')[0].childNodes[0].nodeValue)
            alias = unicode(platform.getElementsByTagName('alias')[0].childNodes[0].nodeValue)
        except:
            logger.warn("Some error parsing platform.")
        
        if platform_id and name:
            platformobj, created = Platform.objects.get_or_create(name=name, defaults={'platform_id': platform_id, 'alias': alias})
            if not created:
                platformobj.platform_id = platform_id
                platformobj.alias = alias
                platformobj.save()
            self.processPlatformDetails.apply_async([self, platform_id, name, alias])

        gamecrawler = GameCrawler(platform_id)
        gamecrawler.crawl.apply_async([gamecrawler])

    @task(ignore_result=True, name="platformDetails")
    def processPlatformDetails(self, platform_id, name, alias):
        try:
            response, content = httplib2.Http().request("http://thegamesdb.net/api/GetPlatform.php?id="+str(platform_id), "GET")
            content = smart_str(content)
            dom = minidom.parseString(content)
            platform = dom.getElementsByTagName('Platform')[0]
            overview = ""
            try:
                overview = unicode(platform.getElementsByTagName('overview')[0].childNodes[0].nodeValue)
            except:
                pass

            developer = ""
            try:
                developer = unicode(platform.getElementsByTagName('developer')[0].childNodes[0].nodeValue)
            except:
                pass

            manufacturer = ""
            try:
                manufacturer = unicode(platform.getElementsByTagName('manufacturer')[0].childNodes[0].nodeValue)
            except:
                pass
            
            cpu = ""
            try:
                cpu = unicode(platform.getElementsByTagName('cpu')[0].childNodes[0].nodeValue)
            except:
                pass

            memory = ""
            try:
                memory = unicode(platform.getElementsByTagName('memory')[0].childNodes[0].nodeValue)
            except:
                pass

            graphics = ""
            try:
                graphics = unicode(platform.getElementsByTagName('graphics')[0].childNodes[0].nodeValue)
            except:
                pass

            sound = ""
            try:
                sound = unicode(platform.getElementsByTagName('sound')[0].childNodes[0].nodeValue)
            except:
                pass

            display = ""
            try:
                display = unicode(platform.getElementsByTagName('display')[0].childNodes[0].nodeValue)
            except:
                pass

            media = ""
            try:
                media = unicode(platform.getElementsByTagName('media')[0].childNodes[0].nodeValue)
            except:
                pass

            maxcontrollers = 1
            try:
                maxcontrollers = int(platform.getElementsByTagName('maxcontrollers')[0].childNodes[0].nodeValue)
            except:
                pass

            youtube_link = ""
            try:
                youtube_link = unicode(platform.getElementsByTagName('Youtube')[0].childNodes[0].nodeValue)
            except:
                pass

            rating = float(0)
            try:
                rating = int(platform.getElementsByTagName('rating')[0].childNodes[0].nodeValue)
            except:
                pass

            baseurl = ""
            try:
                baseurl = dom.getElementsByTagName('baseImgUrl')[0].childNodes[0].nodeValue
            except:
                pass

            ''' For Fan Arts '''
            fanarts_json = ""
            try:
                o_fanarts = []
                t_fanarts = []
                fanartdom = platform.getElementsByTagName('fanart')
                for element in fanartdom:
                    img_orig = baseurl + element.getElementsByTagName('original')[0].childNodes[0].nodeValue
                    img_thumb = baseurl + element.getElementsByTagName('thumb')[0].childNodes[0].nodeValue
                    o_fanarts.append(img_orig)
                    t_fanarts.append(img_thumb)
                    
                o_fanarts_str = '[' + ','.join(['"'+unicode(item)+'"' for item in o_fanarts]) + ']'
                t_fanarts_str = '[' + ','.join(['"'+unicode(item)+'"' for item in t_fanarts]) + ']'
                
                fanarts_json = '{"original": ' + o_fanarts_str + ', "thumbnail": ' + t_fanarts_str + '}'
            except:
                pass

            ''' For Box Arts '''
            boxarts_json = ""
            try:
                o_boxarts = []
                t_boxarts = []
                type_boxarts = []
                boxartdom = platform.getElementsByTagName('boxart')
                for element in boxartdom:
                    img_orig = baseurl + element.childNodes[0].nodeValue
                    #img_thumb = baseurl + element.getAttribute('thumb')
                    img_type = element.getAttribute('side')
                    o_boxarts.append(img_orig)
                    #t_boxarts.append(img_thumb)
                    type_boxarts.append(img_type)
                    
                o_boxarts_str = '[' + ','.join(['"'+unicode(item)+'"' for item in o_boxarts]) + ']'
                #t_boxarts_str = '[' + ','.join(['"'+unicode(item)+'"' for item in t_boxarts]) + ']'
                type_boxarts_str = '[' + ','.join(['"'+unicode(item)+'"' for item in type_boxarts]) + ']'
                
                boxarts_json = '{"original": ' + o_boxarts_str + ', "type": ' + type_boxarts_str + '}'
            except:
                pass
            
            ''' For Banners '''
            banner = ""
            try:
                banner = baseurl + platform.getElementsByTagName('banner')[0].childNodes[0].nodeValue                    
            except:
                pass

            #print platform_id, name, alias, overview, developer, manufacturer, cpu, memory, graphics, sound, display, media, maxcontrollers, youtube_link, rating, baseImgUrl, fanarts_json, boxarts_json, banner

            platformobj, created = Platform.objects.get_or_create(name=name, defaults={'platform_id': platform_id, 'alias': alias, 'maxcontrollers': maxcontrollers, 'rating': rating, 'overview': overview, 'developer': developer, 'manufacturer': manufacturer, 'cpu': cpu, 'memory': memory, 'graphics': graphics, 'sound': sound, 'display': display, 'media': media, 'youtube_link': youtube_link, 'fanarts': fanarts_json, 'boxarts': boxarts_json, 'banner': banner})

            if not created:
                platformobj.platform_id = platform_id
                platformobj.alias = alias
                platformobj.overview = overview
                platformobj.developer = developer
                platformobj.manufacturer = manufacturer
                platformobj.cpu = cpu
                platformobj.memory = memory
                platformobj.graphics = graphics
                platformobj.sound = sound
                platformobj.display = display
                platformobj.media = media
                platformobj.maxcontrollers = maxcontrollers
                platformobj.youtube_link = youtube_link
                platformobj.rating = rating
                platformobj.fanarts = fanarts_json
                platformobj.boxarts = boxarts_json
                platformobj.banner = banner
                platformobj.save()
        except:
            logger.warn("Error getting platforms details.")
            print name


class GameCrawler(object):
    def __init__(self, platform_id):
        self.platform_id = platform_id
    
    @task(ignore_result=True, name="gameList")    
    def crawl(self):
        try:
            response, content = httplib2.Http().request("http://thegamesdb.net/api/GetPlatformGames.php?platform="+str(self.platform_id), "GET")
            content = smart_str(content)
            dom = minidom.parseString(content)
            for game in dom.getElementsByTagName('Game'):
                self.processGame.apply_async([self, game.toxml()], queue="game")
        except:
            logger.warn("Error getting games list.")
    
    @task(ignore_result=True, name="gameDetails")
    def processGame(self, game):
        game = smart_str(game)
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
            title = unicode(game.getElementsByTagName('GameTitle')[0].childNodes[0].nodeValue)
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
            release_date_str = unicode(game.getElementsByTagName('ReleaseDate')[0].childNodes[0].nodeValue)
            release_date = datetime.strptime(release_date_str, '%m/%d/%Y').date()
        except:
            pass
        
        overview = ""
        try:
            overview = unicode(game.getElementsByTagName('Overview')[0].childNodes[0].nodeValue)
        except:
            pass
        
        youtube_link = ""
        try:
            youtube_link = unicode(game.getElementsByTagName('Youtube')[0].childNodes[0].nodeValue)
        except:
            pass
        
        publisher = ""
        try:
            publisher = unicode(game.getElementsByTagName('Publisher')[0].childNodes[0].nodeValue)
        except:
            pass
        
        developer = ""
        try:
            developer = unicode(game.getElementsByTagName('Developer')[0].childNodes[0].nodeValue)
        except:
            pass
        
        esrb = ""
        try:
            esrb = unicode(game.getElementsByTagName('ESRB')[0].childNodes[0].nodeValue)
        except:
            pass
            
        players = 1
        try:
            players = int(game.getElementsByTagName('Players')[0].childNodes[0].nodeValue)
        except:
            pass
        
        co_op = False
        try:
            str_co_op = unicode(game.getElementsByTagName('Co-op')[0].childNodes[0].nodeValue)
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
                
            o_fanarts_str = '[' + ','.join(['"'+unicode(item)+'"' for item in o_fanarts]) + ']'
            t_fanarts_str = '[' + ','.join(['"'+unicode(item)+'"' for item in t_fanarts]) + ']'
            
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
                
            o_screenshots_str = '[' + ','.join(['"'+unicode(item)+'"' for item in o_screenshots]) + ']'
            t_screenshots_str = '[' + ','.join(['"'+unicode(item)+'"' for item in t_screenshots]) + ']'
            
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
                
            o_boxarts_str = '[' + ','.join(['"'+unicode(item)+'"' for item in o_boxarts]) + ']'
            t_boxarts_str = '[' + ','.join(['"'+unicode(item)+'"' for item in t_boxarts]) + ']'
            type_boxarts_str = '[' + ','.join(['"'+unicode(item)+'"' for item in type_boxarts]) + ']'
            
            boxarts_json = '{"original": ' + o_boxarts_str + ', "thumbnail": ' + t_boxarts_str + ', "type": ' + type_boxarts_str + '}'
        except:
            pass
        
        ''' For Banners '''
        banner = ""
        try:
            banner = baseurl + game.getElementsByTagName('banner')[0].childNodes[0].nodeValue
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
        
        #print game_id, title, platform_id, release_date, overview, youtube_link, publisher, developer, esrb, players, co_op, rating, fanarts_json, boxarts_json, screenshots_json, banner, clearlogo
        
        platformobj = Platform.objects.get(platform_id=platform_id)
        logger.warn("Processing game %s on %s platform"%(title, platformobj.name))
        
        gameobj, created = Game.objects.get_or_create(title=title, platform=platformobj, defaults={'game_id': game_id, 'overview': overview, 'esrb': esrb, 'youtube_link': youtube_link, 'release_date': release_date, 'players': players, 'co_op': co_op, 'publisher': publisher, 'developer': developer, 'rating': rating, 'fanarts': fanarts_json, 'screenshots': screenshots_json, 'boxarts': boxarts_json, 'banner': banner, 'clearlogo': clearlogo})
        
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
            gameobj.banner = banner
            gameobj.clearlogo = clearlogo
            gameobj.save()
        
        for genre in genres:
            gameobj.genres.add(genre)
            gameobj.save()
