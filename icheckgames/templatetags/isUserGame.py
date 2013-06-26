from django import template
from icheckgames.models import GameMap
register = template.Library()

'''
	Template tag function to check if the game exists in the
	user's list
'''
@register.simple_tag
def isUserGame(user, obj):
	try:
		user.gamemap_set.get(game=obj)
		return 'checked'
	except:
		return
	