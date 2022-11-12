from flask import jsonify
from .user.models import User

from flask_jwt_extended import get_jwt
from flask_jwt_extended import verify_jwt_in_request

from .extensions import jwt
# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import set_access_cookies
# from flask_jwt_extended import jwt_refresh_token_required

from functools import wraps


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    user = User.objects(id__exact=identity).first()
    if user is not None:
        return user
    return None

@jwt.user_lookup_error_loader
def custom_user_loader_error(identity):
    return jsonify(msg=f"User {identity} not found"), 404

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.additional_claims_loader
def add_claims_to_access_token(identity):
    return {
        "is_administrator": identity.is_administrator,
        "is_moderator": identity.is_moderator,
        # "is_baned": identity.is_baned,
        # "is_active": identity.is_active,
    }

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("is_administrator"):
                return fn(*args, **kwargs)
            else:
                msg='Không đủ quyền truy cập!'
                return {'msg':msg}, 403
        return decorator
    return wrapper

def mod_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("is_moderator") or claims.get("is_administrator"):
                return fn(*args, **kwargs)
            else:
                msg='Không đủ quyền truy cập!'
                return {'msg':msg}, 403
        return decorator
    return wrapper


# @jwt_refresh_token_required
# def refresh_expiring_jwts(response):
#     try:
#         current_user = get_jwt_identity()
#         access_token = create_access_token(identity=current_user)
#         resp = jsonify({'message': 'Token Refreshed!'})
#         set_access_cookies(resp, access_token)
#         return resp
#     except:
#         return jsonify({'error': 'Something went wrong refreshing token'})





# class TokenBlocklist(Document):
#     jti = db.StringField(max_length=36, nullable=False)
#     created_at = db.DateTimeField(nullable=False)


# @jwt.token_in_blocklist_loader
# def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
#     jti = jwt_payload["jti"]
#     token = TokenBlocklist.objects(jti=jti).scalar()

#     return token is not None



