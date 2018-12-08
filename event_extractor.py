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
