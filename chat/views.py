from chat.models import Chat, User

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required

# import redis

chat_limit = 50
@login_required
def chat(request):
    chats = Chat.objects.select_related().all()[0:chat_limit]
    return render(request, 'chat/chat.html', locals())

@csrf_exempt
def chat_api(request):
    try:
        #Get User from sessionid
        session = Session.objects.get(session_key=request.POST.get('sessionid'))
        user_id = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(id=user_id)

        #Create chat message
        Chat.objects.create(user=user, message=request.POST.get('message'))
        
        # Remove the extra chat messages from the table
        chat = Chat.objects.all()
        chat_count = chat.count()
        count = chat_count - chat_limit
        

        while count > 0:
            chat[0].delete()
            count -= 1
        #Once comment has been created post it to the chat channel
        # r = redis.StrictRedis(host='localhost', port=6379, db=0)
        # message = json.dumps({"user": user.username, "message": request.POST.get('comment')})
        # # r.publish('chat', {user.username + ': ' + request.POST.get('comment'))
        # r.publish('chat', message)
        
        return HttpResponse("Everything worked :)")
    except Exception, e:
        print e
        return HttpResponseServerError(str(e))