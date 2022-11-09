from flask import jsonify
from .user import User

from .extensions import jwt
# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import set_access_cookies
# from flask_jwt_extended import jwt_refresh_token_required


# user = User()

@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    if not User.objects(username__exact=identity):
        return None
    return User.objects(username__exact=identity).get()


@jwt.user_loader_error_loader
def custom_user_loader_error(identity):
    return jsonify(msg=f"User {identity} not found"), 404

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