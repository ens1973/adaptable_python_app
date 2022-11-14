from marshmallow import EXCLUDE
from marshmallow_mongoengine import ModelSchema
from .models import Product

class ProductSchema(ModelSchema):
    class Meta:
        model = Product
        unknown = EXCLUDE
        load_instance = True

product_schema = ProductSchema()
product_schema_many = ProductSchema(many=True)