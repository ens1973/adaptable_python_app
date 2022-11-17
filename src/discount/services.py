from flask import jsonify
from .models import Discount as Item
from .schemas import discount_schema as schema
from .schemas import discount_schema_many as schema_many

def does_not_exist(item_id):
    model_name = "Discount"
    return f"{model_name} with ID {item_id} does not exist"

def create_item(data):
    """Given serialized data, deserialize it and create a new item"""
    items = schema_many.load(data)
    Item.objects.insert(items)
    return schema_many.dump(items), 201


def get_all_items():
    """Deserialize and return all items in database"""
    return get_all_items_from_page(1)


def get_all_items_from_page(page_num):
    """Deserialize and return all items in database"""
    
    total_item = Item.objects.count()
    item_per_page = Item.item_per_page
    extra_page = 1 if total_item % item_per_page > 0 else 0
    total_page = total_item // item_per_page + extra_page

    skip_item = (page_num - 1) * item_per_page
    items = schema_many.dump(Item.objects.skip(skip_item).limit(item_per_page))
    return {
        'items': items, 
        'total_page': total_page,
        'current_page': page_num
    }, 200
    # print(Item.objects.all())
    # return "hi", 200


def get_item(item_id):
    """Given an item ID, return a serialized item object"""
    if not (item := Item.objects(id=item_id).first()):
        return {"message": does_not_exist(item_id)}, 404

    return schema.dump(item), 200

def get_item_by_code(item_code):
    """Given an item ID, return a serialized item object"""
    if not (item := Item.objects(name__exact=item_code).first()):
        return {"message": does_not_exist(item_code)}, 404

    return schema.dump(item), 200


def update_item(item_id, data):
    if not (item := Item.objects(id=item_id).first()):
        return {"message": does_not_exist(item_id)}, 404

    schema.update(item, data)
    item.save()
    return schema.dump(item), 200


def delete_item(item_id):
    if not (item := Item.objects(id=item_id).first()):
        return {"message": does_not_exist(item_id)}, 404

    item.delete()
    return "Done!", 204
