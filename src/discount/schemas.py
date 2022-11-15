from marshmallow import EXCLUDE
from marshmallow_mongoengine import ModelSchema
from .models import Discount

class DiscountSchema(ModelSchema):
    class Meta:
        model = Discount
        unknown = EXCLUDE
        load_instance = True

discount_schema = DiscountSchema()
discount_schema_many = DiscountSchema(many=True)