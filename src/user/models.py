import mongoengine as me
# from src.extensions import db
# from src.db import Document
from src.rsa import decode_data
from src.rsa import encode_data

class User(me.Document):
    email = me.EmailField(max_length=255, unique=True)
    username = me.StringField(max_length=255, unique=True)
    firstname = me.StringField(max_length=255)
    lastname = me.StringField(max_length=255)
    password = me.StringField(max_length=255)
    profile = me.ListField(me.DictField())
    is_administrator = me.BooleanField(required=True, default=False)
    is_moderator = me.BooleanField(required=True, default=False)
    is_baned = me.BooleanField(required=True, default=False)
    is_active = me.BooleanField(required=True, default=True)
    confirmed_at = me.DateTimeField()

    def __repr__(self):
        return f'<User (username={self.username})>'

    @staticmethod
    def hash_password(password):
        return encode_data(password)

    @staticmethod
    def unhash_password(password):
        return decode_data(password)

    @staticmethod
    def verify_password(password, hashed_password):
        if password == decode_data(hashed_password):
            return True
        return False

