from flask import request
from flask_restx import Namespace
from flask_restx import Resource
from flask_restx import fields
from flask_jwt_extended import jwt_required
from src.jwt import admin_required

from .services import create_item
from .services import get_all_items
from .services import get_item
from .services import update_item
from .services import delete_item

api = Namespace("users", description="User related operations !")

body_fields = api.model(
    "User", {
        "firstname": fields.String(required=False, description="Your first name"),
        "lastname": fields.String(required=False, description="Your last name"),
        "username": fields.String(required=True, description="Your username, it's required"),
        "password": fields.String(required=True, description="Your password, it's required"),
        "email": fields.String(required=True, description="Your email, it's required"),
        "is_administrator": fields.Boolean(required=True, description="administrator role", default=False),
        "is_moderator": fields.Boolean(required=True, description="moderator role", default=False),
        "is_baned": fields.Boolean(required=True, description="baned status", default=False),
        "is_active": fields.Boolean(required=True, description="active status", default=True)
    }
)


@api.route('')
class UserList(Resource):
    @jwt_required()
    def get(self):
        """Get a list"""
        return get_all_items()

    @api.doc(body=body_fields)
    def post(self):
        """Create new"""
        return create_item(request.get_json())


@api.route('/<string:item_id>')
class User(Resource):
    @admin_required()
    def get(self, item_id):
        """Get by single ID"""
        return get_item(item_id)

    @api.doc(body=body_fields)
    @jwt_required()
    def put(self, item_id):
        """Update by single ID"""
        return update_item(item_id, request.get_json())

    @jwt_required()
    def delete(self, item_id):
        """Delete by single ID"""
        return delete_item(item_id)


# api.add_resource(UserList, "") # can use @api.route('') before Class define
# api.add_resource(User, "/<string:item_id>")
