from django.contrib import admin
from models import Platform, Game, Genre

class PlatformAdmin(admin.ModelAdmin):
	list_display = ('platform_id', 'name', 'alias')
	search_fields = ('alias',)

class GameAdmin(admin.ModelAdmin):
	list_display = ('game_id', 'title', 'platform', 'release_date', 'developer', 'publisher')
	search_fields = ('title',)
	list_filter = ('genres', 'platform',)


admin.site.register(Platform, PlatformAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Genre)