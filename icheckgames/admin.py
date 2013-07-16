from django.contrib import admin
from models import UserProfile, Platform, Game, Genre, GameMap

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'cover', 'facebookUser', 'facebookId', 'facebookToken')

class PlatformAdmin(admin.ModelAdmin):
	list_display = ('platform_id', 'name', 'alias')
	search_fields = ('alias',)

class GameAdmin(admin.ModelAdmin):
	list_display = ('game_id', 'title', 'platform', 'release_date', 'developer', 'publisher')
	search_fields = ('title',)
	list_filter = ('genres', 'platform',)

class GameMapAdmin(admin.ModelAdmin):
        list_display = ('user', 'game', 'owned', 'status', 'favorite', 'wish')
        search_fields = ('game',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Genre)
admin.site.register(GameMap, GameMapAdmin)