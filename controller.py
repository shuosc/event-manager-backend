import hug
from model import *
from pony.orm import *

@hug.get("/example")
def example():
    return {'response': 'example'}

@hug.post("/event")
def postEvent(body: hug.types.json):
    with db_session:
        event = Event(eventName=body['eventName'], lecturer=body['lecturer'], eventTime=body['eventTime'], eventPlace=body['eventPlace'])
        commit()
        return {'response': 200}

@hug.get("/event")
def getEvent():
    with db_session:
        events = Event.select()
        result = []
        for event in events:
            result.append({'eventName': event.eventName, 'lecturer': event.lecturer, 'eventTime': event.eventTime, 'eventPlace':event.eventPlace})
        return result
@hug.get("/event/{id}")
def getEventDetail(id: hug.types.number):
    with db_session:
        eventDetail = select(c for c in Event if c.id == id)
        result = []
        for event in eventDetail:
            result.append({'eventName': event.eventName, 'lecturer': event.lecturer, 'eventTime': event.eventTime, 'eventPlace':event.eventPlace})
        return result