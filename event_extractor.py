import facebook
import datetime

#compares two dates, if eventTime is before now date returns false, otherwise returns true
def dateComapration(eventTime, now):
    ey=eventTime[:4]
    ny=now[:4]
    if(ey>ny):
        return True
    if(ey<ny):
        return False
    em=eventTime[5:7]
    nm=now[5:7]
    if(em>nm):
        return True
    if(em<nm):
        return False
    ed=eventTime[8:10]
    nd=now[8:10]
    if(ed<nd):
        return False
    return True



#your personal token
token= ''

graph = facebook.GraphAPI(access_token=token, version = 3.1)
events = graph.request('me?fields=events')
eventList = events['events']
eventData = eventList['data']

now = datetime.datetime.now()

for index in range(0,len(eventData)):
    event = eventData[index]
    starttime=event['start_time']
    if(dateComapration(starttime, now.strftime("%Y-%m-%d"))):
       print(event['name'])

#!/usr/bin/python
# coding: utf-8

import facebook
import urllib
import urlparse
import subprocess
import warnings

# Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
warnings.filterwarnings('ignore', category=DeprecationWarning)


# Parameters of your app and the id of the profile you want to mess with.
FACEBOOK_APP_ID     = 'XXXXXXXXXXXXXXX'
FACEBOOK_APP_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
FACEBOOK_PROFILE_ID = 'XXXXXX'


# Trying to get an access token. Very awkward.
oauth_args = dict(client_id     = FACEBOOK_APP_ID,
                  client_secret = FACEBOOK_APP_SECRET,
                  grant_type    = 'client_credentials')
oauth_curl_cmd = ['curl',
                  'https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args)]
oauth_response = subprocess.Popen(oauth_curl_cmd,
                                  stdout = subprocess.PIPE,
                                  stderr = subprocess.PIPE).communicate()[0]

try:
    oauth_access_token = urlparse.parse_qs(str(oauth_response))['access_token'][0]
except KeyError:
    print('Unable to grab an access token!')
    exit()

facebook_graph = facebook.GraphAPI(oauth_access_token)


# Try to post something on the wall.
try:
    fb_response = facebook_graph.put_wall_post('Hello from Python', \
                                               profile_id = FACEBOOK_PROFILE_ID)
    print (fb_response)
except facebook.GraphAPIError as e:
    print ('Something went wrong:', e.type, e.message)