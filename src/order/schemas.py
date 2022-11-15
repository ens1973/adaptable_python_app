from marshmallow import EXCLUDE
from marshmallow_mongoengine import ModelSchema
from .models import Order

class OrderSchema(ModelSchema):
    class Meta:
        model = Order
        unknown = EXCLUDE
        load_instance = True

order_schema = OrderSchema()
order_schema_many = OrderSchema(many=True)