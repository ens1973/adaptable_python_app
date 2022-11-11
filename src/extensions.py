
from mongoengine import connect
from mongoengine import register_connection
from os import getenv

def db_init(env):
    # db =  connect(
    #     db=getenv('DATABASE_NAME'), 
    #     host=getenv('DATABASE_HOST'), 
    #     username=getenv('DATABASE_USERNAME'),
    #     password=getenv('DATABASE_PASSWORD'),
    #     authentication_source=getenv('DATABASE_AUTH')
    #     )
    if (env == 'development'):
        db =  connect(host=getenv('DEV_DATABASE_URL'))
        register_connection(alias='default', db=getenv('DEV_DATABASE_NAME'))
    else:
        db =  connect(host=getenv('DATABASE_URL'))
        register_connection(alias='default', db=getenv('DATABASE_NAME'))


# from flask_marshmallow import Marshmallow
# from marshmallow_mongoengine import Marshmallow
# ma = Marshmallow()

# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
# from flask_mongoengine import MongoEngine
# db = MongoEngine()

from flask_jwt_extended import JWTManager
jwt = JWTManager()

