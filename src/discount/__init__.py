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
from .services import get_item_by_code
from .services import update_item
from .services import delete_item

api = Namespace("discount", description="Discount related operations !")


discount_fields = api.model(
    "Discount", {
        'code': fields.String(required=True, description='Discount code'),
        'percent': fields.Float(required=True, default=0, description='Discount percent'),
        'amount': fields.Float(required=True, default=0, description='Discount amount'),
        'mfg_at': fields.DateTime(description='Mfg at'),
        'exp_at': fields.DateTime(description='Exp at')
    }
)


@api.route('')
class DiscountList(Resource):
    @mod_required()
    def get(self):
        """Get a list"""
        return get_all_items()

    @api.doc(body=[discount_fields])
    @mod_required()
    def post(self):
        """Create new"""
        return create_item(request.get_json())

@api.route('/page/<int:page_number>')
class DiscountListWithPage(Resource):
    @mod_required()
    def get(self, page_number):
        """Get a list"""
        return get_all_items_from_page(page_number)


@api.route('/<string:item_id>')
class Discount(Resource):
    def get(self, item_id):
        """Get by single ID"""
        return get_item(item_id)

    @api.doc(body=discount_fields)
    @mod_required()
    def put(self, item_id):
        """Update by single ID"""
        return update_item(item_id, request.get_json())

    @mod_required()
    def delete(self, item_id):
        """Delete by single ID"""
        return delete_item(item_id)

@api.route('/code/<string:item_code>')
class DiscountByCode(Resource):
    def get(self, item_code):
        """Get by single ID"""
        return get_item_by_code(item_code)

