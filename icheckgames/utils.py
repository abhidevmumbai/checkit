import httplib2
from urlparse import parse_qs
from django.conf import settings

def getAccessToken(code):
    try:
        http = httplib2.Http()
        facebook_oauth_url = 'https://graph.facebook.com/oauth/access_token?client_id=' + settings.FACEBOOK_APP_ID + '&redirect_uri=' + settings.FACEBOOK_REDIRECT_URI + '&client_secret=' + settings.FACEBOOK_APP_SECRET + '&code=' + code
        response, content = http.request(facebook_oauth_url, "GET")
        parameters = parse_qs(content)
        return parameters['access_token'][0]
    except:
        return None