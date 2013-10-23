from django.contrib import admin
from models import Chat

class ChatAdmin(admin.ModelAdmin):
    list_display = ('user', 'message')

admin.site.register(Chat, ChatAdmin)