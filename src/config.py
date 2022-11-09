# from .extensions import db
from os import getenv

class Config:
    TESTING = False
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # DEFAULT_CONNECTION_NAME = db
    SEND_FILE_MAX_AGE_DEFAULT = 0
    JWT_TOKEN_LOCATION = ["headers", "query_string", "json"]
    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
    # MONGODB_SETTINGS = [
    #     {
    #         "db": getenv('DB_NAME'),
    #         "host": getenv('MONGODB_URL'),
    #         # "port": 27017,
    #         "alias": "default",
    #     }
    # ]


class DevelopmentConfig(Config):
    ENV = getenv('ENV')
    DEBUG = getenv('DEBUG')
    SQLALCHEMY_DATABASE_URI = "sqlite:///../dev-db.sqlite"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///../test-db.sqlite"


class ProductionConfig(Config):
    DEBUG = 0
    SQLALCHEMY_DATABASE_URI = "sqlite:///../prod-db.sqlite"
