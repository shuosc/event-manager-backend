from pony.orm import *
from datetime import datetime

db = Database()
db.bind(provider='mysql', host='localhost', user='jackjack59', passwd='jackjack123', db='eventmanager')

class Event(db.Entity):
    id = PrimaryKey(int, auto=True)
    eventName = Required(str)
    lecturer = Required(str)
    eventTime = Optional(str)
    eventPlace = Optional(str)
    createTime = Required(datetime, sql_default='CURRENT_TIMESTAMP')


db.generate_mapping(create_tables=True)