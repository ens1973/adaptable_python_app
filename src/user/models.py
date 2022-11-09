# import mongoengine as me
from src.extensions import db
from src.db import Document
from src.rsa import decode_data
from src.rsa import encode_data

class User(Document):
    email = db.StringField(max_length=255, unique=True)
    username = db.StringField(max_length=255, unique=True)
    firstname = db.StringField(max_length=255)
    lastname = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()

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

