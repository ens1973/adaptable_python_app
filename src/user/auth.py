from flask import request
from flask_restx import Namespace
from flask_restx import Resource
from flask_restx import fields

from flask_jwt_extended import jwt_required

from .auth_services import refresh_token
from .auth_services import registration
from .auth_services import login
from .auth_services import logout

api = Namespace("auth", description="User auth related operations !")

body_fields = api.model(
    "AuthUser", {
        'username': fields.String(required=True, description='Username'),
        'password': fields.String(required=True, description='Password'),
    }
)



@api.route('/registration')
# @api.doc(False)
class UserRegistration(Resource):
    @api.doc(body=body_fields)
    def post(self):
        return registration(request.get_json())


@api.route('/login')
class UserLogin(Resource):
    @api.doc(body=body_fields)
    def post(self):
        return login(request.get_json())


@api.route('/logout')
class UserLogout(Resource):
    @jwt_required()
    def delete(self):
        return logout()


# @api.route('/token/refresh')
# class TokenRefresh(Resource):
#     @jwt_refresh_token_required
#     def post(self):
#         return refresh_token()


# api.add_resource(UserList, "")
# api.add_resource(User, "/<string:item_id>")
