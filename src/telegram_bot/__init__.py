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
from .services import get_item_by_name
from .services import update_item
from .services import delete_item

api = Namespace("telegrambot", description="Telegram Bot related operations !")


telegram_bot_fields = api.model(
    "TelegramBot", {
        'name': fields.String(required=True, description='Name'),
        'bot_key': fields.String(required=True, description='Bot key'),
        'group_id': fields.String(required=True, description='Group id'),
    }
)


@api.route('')
class TelegramBotList(Resource):
    @mod_required()
    def get(self):
        """Get a list"""
        return get_all_items()

    @api.doc(body=[telegram_bot_fields])
    @mod_required()
    def post(self):
        """Create new"""
        return create_item(request.get_json())

@api.route('/page/<int:page_number>')
class TelegramBotListWithPage(Resource):
    @mod_required()
    def get(self, page_number):
        """Get a list"""
        return get_all_items_from_page(page_number)


@api.route('/<string:item_id>')
class TelegramBot(Resource):
    def get(self, item_id):
        """Get by single ID"""
        return get_item(item_id)

    @api.doc(body=telegram_bot_fields)
    @mod_required()
    def put(self, item_id):
        """Update by single ID"""
        return update_item(item_id, request.get_json())

    @mod_required()
    def delete(self, item_id):
        """Delete by single ID"""
        return delete_item(item_id)

@api.route('/name/<string:item_name>')
class TelegramBotByName(Resource):
    def get(self, item_name):
        """Get by single ID"""
        return get_item_by_name(item_name)

