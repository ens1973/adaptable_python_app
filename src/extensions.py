from mongoengine import connect
from mongoengine import register_connection
from os import getenv

import json
from bson.json_util import ObjectId

from flask_jwt_extended import JWTManager

jwt = JWTManager()

def db_init(env):
    if (env == 'development'):
        db =  connect(host=getenv('DEV_DATABASE_URL'))
        register_connection(alias='default', db=getenv('DEV_DATABASE_NAME'))
    else:
        db =  connect(host=getenv('DATABASE_URL'))
        register_connection(alias='default', db=getenv('DATABASE_NAME'))

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(CustomEncoder, self).default(obj)

# from flask_marshmallow import Marshmallow
# from marshmallow_mongoengine import Marshmallow
# ma = Marshmallow()

# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
# from flask_mongoengine import MongoEngine
# db = MongoEngine()