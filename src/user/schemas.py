from marshmallow import EXCLUDE
from marshmallow_mongoengine import ModelSchema
from .models import User

class UserSchema(ModelSchema):
    class Meta:
        model = User
        unknown = EXCLUDE
        load_instance = True

user_schema = UserSchema()
user_schema_many = UserSchema(many=True)