from marshmallow import EXCLUDE
from marshmallow_mongoengine import ModelSchema
from .models import TelegramBot

class TelegramBotSchema(ModelSchema):
    class Meta:
        model = TelegramBot
        unknown = EXCLUDE
        load_instance = True

telegrambot_schema = TelegramBotSchema()
telegrambot_schema_many = TelegramBotSchema(many=True)