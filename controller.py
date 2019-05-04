import hug
from model import *
from pony.orm import *

@hug.post("/event")
def event(body: hug.types.json):
    with db_session:
        event = Event(eventName=body['eventName'])
        commit()
        return {'response': 200}
