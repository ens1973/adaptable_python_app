from flask import request
from flask_restx import Namespace
from flask_restx import Resource
from flask_restx import fields
from flask_jwt_extended import jwt_required
from .services import create_item
from .services import get_all_items
from .services import get_item
from .services import update_item
from .services import delete_item

api = Namespace("users", description="User related operations !")

body_fields = api.model(
    "User", {
        'username': fields.String(required=True, description='Username'),
        'password': fields.String(required=True, description='Password'),
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


class User(Resource):
    def get(self, item_id):
        """Get by single ID"""
        return get_item(item_id)

    @api.doc(body=body_fields)
    def put(self, item_id):
        """Update by single ID"""
        return update_item(item_id, request.get_json())

    def delete(self, item_id):
        """Delete by single ID"""
        return delete_item(item_id)


# api.add_resource(UserList, "")
api.add_resource(User, "/<string:item_id>")
