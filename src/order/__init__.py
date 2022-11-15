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


api = Namespace("order", description="Order related operations !")


order_item_specs_fields = api.model(
    "OrderItemSpecs", {
        'key': fields.String(description='Specs key'),
        'value': fields.String(description='Specs value'),
    }
)

order_item_fields = api.model(
    "OrderItem", {
        'name': fields.String(required=True, description='Product name'),
        'sku': fields.String(description='Product SKU'),
        'price': fields.Float(required=True, default=1, description='Price'),
        'short_description': fields.String(description='Short description'),
        'description': fields.String(description='Description'),
        'specs': fields.List(fields.Nested(order_item_specs_fields)),
        'quantity': fields.Integer(required=True, default=1, description='Quantity'),
    }
)

order_fields = api.model(
    "Order", {
        'customer_name': fields.String(required=True, description='Customer name'),
        'customer_phone': fields.String(required=True, description='Customer phone'),
        'customer_address': fields.String(required=True, description='Customer address'),
        'receiver_name': fields.String(required=True, description='Receiver name'),
        'receiver_phone': fields.String(required=True, description='Receiver phone'),
        'receiver_address': fields.String(required=True, description='Receiver address'),
        'items': fields.List(fields.Nested(order_item_fields)),
        'note': fields.String(description='Note'),
        'total_quantity': fields.Integer(required=True, default=1, description='Total quantity'),
        'price': fields.Float(required=True, default=1, description='Price'),
        'discount': fields.Float(required=True, default=0, description='Discount'),
        'total_price': fields.Float(required=True, default=1, description='Total price'),
        'paid': fields.Boolean(required=True, default=False, description='Paid'),
        'type': fields.Integer(required=True, default=1, description='type'),
        'status': fields.Integer(required=True, default=0, description='Status'),
    }
)


@api.route('')
class OrderList(Resource):
    def get(self):
        """Get a list"""
        return get_all_items()

    @api.doc(body=[order_fields])
    @mod_required()
    def post(self):
        """Create new"""
        return create_item(request.get_json())

@api.route('/page/<int:page_number>')
class OrderListWithPage(Resource):
    # @jwt_required()
    def get(self, page_number):
        """Get a list"""
        return get_all_items_from_page(page_number)


@api.route('/<string:item_id>')
class Order(Resource):
    def get(self, item_id):
        """Get by single ID"""
        return get_item(item_id)

    @api.doc(body=order_fields)
    @mod_required()
    def put(self, item_id):
        """Update by single ID"""
        return update_item(item_id, request.get_json())

    @mod_required()
    def delete(self, item_id):
        """Delete by single ID"""
        return delete_item(item_id)

