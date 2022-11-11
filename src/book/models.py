import mongoengine as me
# from src.extensions import db_init

# db_init()

class Book(me.Document):
    title = me.StringField()
