from flask import jsonify
from .models import User as Item
from .schemas import user_schema as schema
from .schemas import user_schema_many as schema_many
from .schemas import security_user_schema as security_schema
from .schemas import security_user_schema_many as security_schema_many

model_name = "User"

def does_not_exist(item_id):
    return f"{model_name} with ID {item_id} does not exist"

def create_item(data):
    """Given serialized data, deserialize it and create a new item"""
    items = schema_many.load(data)
    for item in items:
        item.password = Item().hash_password(item.password)
    Item.objects.insert(items)
    return security_schema_many.dump(items), 201


def get_all_items():
    """Deserialize and return all items in database"""
    # print(security_schema_many.dump(Item.objects.all()))
    # return "hi", 200
    return security_schema_many.dump(Item.objects.all()), 200


def get_item(item_id):
    """Given an item ID, return a serialized item object"""
    if not (item := Item.objects(id=item_id).first()):
        return {"message": does_not_exist(item_id)}, 404

    return security_schema.dump(item), 200


def update_item(item_id, data):
    if not (item := Item.objects(id=item_id).first()):
        return {"message": does_not_exist(item_id)}, 404

    schema.update(item, data)
    item.save()
    return security_schema.dump(item), 200


def delete_item(item_id):
    if not (item := Item.objects(id=item_id).first()):
        return {"message": does_not_exist(item_id)}, 404

    item.delete()
    return "Done!", 204
