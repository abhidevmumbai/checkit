from django import template
try: import simplejson as json
except ImportError: import json

register = template.Library()


'''
	Template tag function to parse the Image json 
	based on the key supplied
'''
@register.simple_tag
def parseImagejson(obj, filter):
	json_obj = json.loads(obj)

	try:
		if filter == 'original':
			return json_obj['original'][0]
		elif filter == 'thumbnailFront':
			index = json_obj['type'].index('front')
			return json_obj['thumbnail'][index]
		elif filter == 'thumbnailBack':
			index = json_obj['type'].index('back')
			return json_obj['thumbnail'][index]
	except:
		return '../static/img/default_game_icon2.png'