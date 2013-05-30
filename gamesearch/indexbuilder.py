from models import GameKeyword
from icheckgames.models import Game

from celery import task

import logging
logger = logging.getLogger(__name__)

import re

try: import simplejson as json
except ImportError: import json

class IndexBuilder(object):
    @task(ignore_result=True, name="IndexBuilder")
    def build(self):
        logger.warn("Started building index.")
        for game in Game.objects.all():
            self.processForWords.apply_async([self, game], queue="word")

    @task(ignore_result=True, name="processWords")
    def processForWords(self, game):
        logger.warn("Processing game %s for indexing"%(game.title))
        keywords_list = self.getWords(game)
        
        for word in keywords_list:
            try:
                keywordobj, created = GameKeyword.objects.get_or_create(word=word)
                keywordobj.games.add(game)
            except:
                logger.warn("Error in creating a keyword entry.")
        
    def getWords(self, game):
        words_list = re.compile('[\w]+').findall(game.title)
        words = [element.lower() for element in words_list]
        overview_words_list = re.compile('[\w]+').findall(game.overview)
        overview_words = [element.lower() for element in overview_words_list]
        return list(set(words) | set(overview_words))