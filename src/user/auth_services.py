# from flask import jsonify
from .models import User as Item
# from .schemas import user_schema as schema
# from .schemas import user_schema_many as schema_many
from .schemas import security_user_schema as security_schema
from .schemas import security_user_schema_many as security_schema_many
from .services import create_item

from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import set_refresh_cookies
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import get_jwt
# from flask_jwt_extended import jwt_refresh_token_required

from .auth_models import TokenBlocklist
from datetime import datetime
from datetime import timezone
from os import getenv

def registration(data):
    data['is_administrator'] = False
    data['is_moderator'] = False
    admin_key = data.get('admin_key')
    if admin_key == getenv('JWT_SECRET_KEY'):
        data['is_administrator'] = True
        data['is_moderator'] = True
    return create_item([data])

def login(data):
    username = data.get('username')
    password = data.get('password')
    current_user = Item.objects(username__exact=username).first()
    if not current_user:
        return {'message': f"User {username} doesn't exist"}

    if Item().verify_password(password, current_user.password):
        access_token = create_access_token(identity=current_user)
        refresh_token = create_refresh_token(identity=current_user)

        message = f'Logged in as {current_user.username}'

        # set_access_cookies(jsonify(message=message), access_token)
        # set_refresh_cookies(jsonify(message=message), refresh_token)
        dump_security_current_user = security_schema.dump(current_user)
        # dump_current_user['password'] = ''
        return {
            'msg': message,
            'access_token_api': f"apiKey {access_token}",
            'access_token_bearer': f"Bearer {access_token}",
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': dump_security_current_user
        }, 200

    else:
        return {'message': 'Wrong credentials'}

def logout():

    token = get_jwt()
    jti = token["jti"]
    ttype = token["type"]
    now = datetime.now(timezone.utc)
    try:
        block = TokenBlocklist(jti=jti, type=ttype, created_at=now)
        block.save()
    except Exception as e:
        return {'msg': 'Something went wrong deleting token'}, 500
    return {'Logout': True}, 200

    # try:
    #     resp = jsonify({'logout': True})
    #     unset_jwt_cookies(resp)
    #     return {'logout': True}
    # except:
    #     return jsonify({'error': 'Something went wrong deleting token'})
            

def refresh_token():
    try:
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        # set_access_cookies(resp, access_token)
        return {'message': 'Token Refreshed!'}
    except:
        return {'error': 'Something went wrong refreshing token'}
