from flask import request
from flask_restx import Namespace
from flask_restx import Resource
from flask_restx import fields
from flask_jwt_extended import jwt_required
from src.jwt import mod_required
from .services import create_item
from .services import get_all_items
from .services import get_all_items_from_page
from .services import get_item
from .services import update_item
from .services import delete_item

api = Namespace("products", description="Product related operations !")


productspecs_fields = api.model(
    "ProductSpecs", {
        'key': fields.String(description='Specs key'),
        'value': fields.String(description='Specs value'),
    }
)

product_fields = api.model(
    "Product", {
        'name': fields.String(required=True, description='Product name'),
        'price': fields.Float(required=True, description='Price'),
        'short_description': fields.String(description='Short description'),
        'description': fields.String(description='Description'),
        'specs': fields.List(fields.Nested(productspecs_fields)),
    }
)


@api.route('')
class ProductList(Resource):
    def get(self):
        """Get a list"""
        return get_all_items()

    @api.doc(body=[product_fields])
    @mod_required()
    def post(self):
        """Create new"""
        return create_item(request.get_json())

@api.route('/<string:product_filter>/page/<int:page_number>')
class ProductListWithPage(Resource):
    # @jwt_required()
    def get(self, product_filter, page_number):
        """Get a list"""
        return get_all_items_from_page(page_number, product_filter)


@api.route('/<string:item_id>')
class Product(Resource):
    def get(self, item_id):
        """Get by single ID"""
        return get_item(item_id)

    @api.doc(body=product_fields)
    @mod_required()
    def put(self, item_id):
        """Update by single ID"""
        return update_item(item_id, request.get_json())

    @mod_required()
    def delete(self, item_id):
        """Delete by single ID"""
        return delete_item(item_id)

