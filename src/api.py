from flask import Blueprint
from flask_restx import Api

from os import getenv
JWT_HEADER_NAME = getenv('JWT_HEADER_NAME')
JWT_HEADER_TYPE = getenv('JWT_HEADER_TYPE')
JWT_QUERY_STRING_VALUE_PREFIX = getenv('JWT_QUERY_STRING_VALUE_PREFIX')

authorizations = {
    f"{JWT_QUERY_STRING_VALUE_PREFIX}": 
        {"type": JWT_HEADER_TYPE, "in": "header", "name": JWT_HEADER_NAME}
    }

api_bp = Blueprint("api", __name__)
api = Api(
    api_bp, 
    title="REST API", 
    description="A REST API backend", 
    authorizations=authorizations, 
    security=JWT_QUERY_STRING_VALUE_PREFIX
    )


from .health import api as health_ns
api.add_namespace(health_ns)

# from .book import api as book_ns
# api.add_namespace(book_ns)

from .user import api as user_ns
api.add_namespace(user_ns)

from .user.auth import api as auth_ns
api.add_namespace(auth_ns)

from .product import api as product_ns
api.add_namespace(product_ns)

from .order import api as order_ns
api.add_namespace(order_ns)

from .discount import api as discount_ns
api.add_namespace(discount_ns)

from .telegram_bot import api as telegram_bot_ns
api.add_namespace(telegram_bot_ns)


