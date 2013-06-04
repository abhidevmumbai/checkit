from models import GameKeyword
from icheckgames.models import Game

from celery import task

import logging
logger = logging.getLogger(__name__)

import re

try: import simplejson as json
except ImportError: import json

import stemmers

class IndexBuilder(object):
    @task(ignore_result=True, name="IndexBuilder")
    def build(self):
        logger.warn("Started building index.")
        for game in Game.objects.all():
            self.processForWords.apply_async([self, game], queue="word")

    @task(ignore_result=True, name="processWords")
    def processForWords(self, game):
        logger.warn("Processing game %s for indexing"%(game.title))
        title_keywords_list, other_keywords_list = self.getWords(game)
        
        for word in title_keywords_list:
            try:
                keywordobj, created = GameKeyword.objects.get_or_create(word=word)
                keywordobj.title_games.add(game)
            except:
                logger.warn("Error in creating a keyword entry for title words.")
        
        for word in other_keywords_list:
            try:
                keywordobj, created = GameKeyword.objects.get_or_create(word=word)
                keywordobj.other_games.add(game)
            except:
                logger.warn("Error in creating a keyword entry for other words.")
        
    def getWords(self, game):
        stemmer = stemmers.CustomStemmer()
        title_words_list = re.compile('[\w]+').findall(game.title)
        title_words = []
        for element in title_words_list:
            t_word = stemmer.stem(element)
            if t_word:
                title_words.append(t_word)

        overview_words_list = re.compile('[\w]+').findall(game.overview)
        overview_words = []
        for element in overview_words_list:
            o_word = stemmer.stem(element)
            if o_word:
                overview_words.append(o_word)
        return title_words, list(set(overview_words).difference(set(title_words)))
