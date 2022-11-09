from flask import jsonify
from .models import User
from .schemas import user_schema as schema
from .schemas import user_schema_many as schema_many

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

# model_name = "User"

# def does_not_exist(item_id):
#     return f"{model_name} with ID {item_id} does not exist"

# def create_item(data):
#     """Given serialized data, deserialize it and create a new item"""
#     items = schema_many.load(data)
#     for item in items:
#         item.password = Item().hash_password(item.password)
#         item.save()
#     return schema_many.dump(items), 201


# def get_all_items():
#     """Deserialize and return all items in database"""
#     return schema_many.dump(Item.objects.all()), 200


# def get_item(item_id):
#     """Given an item ID, return a serialized item object"""
#     if not (item := Item.objects(id=item_id).first()):
#         return {"message": does_not_exist(item_id)}, 404

#     return schema.dump(item), 200


# def update_item(item_id, data):
#     if not (item := Item.objects(id=item_id).first()):
#         return {"message": does_not_exist(item_id)}, 404

#     schema.update(item, data)
#     item.save()
#     return schema.dump(item), 200


# def delete_item(item_id):
#     if not (item := Item.objects(id=item_id).first()):
#         return {"message": does_not_exist(item_id)}, 404

#     item.delete()
#     return "Done!", 204


def registration(data):
    pass
    # try:
    #     user.username = data['username']
    #     user.password = user.generate_hash(data['password'])
    #     user.save()

    #     access_token = create_access_token(identity=data['username'])
    #     refresh_token = create_refresh_token(identity=data['username'])

    #     resp = jsonify({
    #         'message': 'User {} was created'.format(data['username'])
    #     })

    #     set_access_cookies(resp, access_token)
    #     set_refresh_cookies(resp, refresh_token)

    #     return resp
    # except Exception as e:
    #     if "E11000 duplicate key error collection" in e.args[0]:
    #         return {'message': 'User {} already exists'.format(data['username'])}
    #     else:
    #         return {'message': 'Oops'}

def login(data):
    username = data.get('username')
    password = data.get('password')
    current_user = User.objects(username__exact=username).first()
    if not current_user:
        return {'message': f"User {username} doesn't exist"}

    if User().verify_password(password, current_user.password):
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)

        message = f'Logged in as {current_user.username}'

        # set_access_cookies(jsonify(message=message), access_token)
        # set_refresh_cookies(jsonify(message=message), refresh_token)
        print(schema.dump(current_user))
        return {
            'msg': message,
            'access_token_bearer': f"Bearer {access_token}",
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': schema.dump(current_user)
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
        resp = jsonify({'message': 'Token Refreshed!'})
        set_access_cookies(resp, access_token)
        return resp
    except:
        return jsonify({'error': 'Something went wrong refreshing token'})
