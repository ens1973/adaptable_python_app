from flask import Blueprint
from flask_restx import Api

authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api_bp = Blueprint("api", __name__)
api = Api(api_bp, title="REST API", description="A REST API backend", authorizations=authorizations, security='Bearer')


from .health import api as health_ns
api.add_namespace(health_ns)

from .book import api as book_ns
api.add_namespace(book_ns)

from .user import api as user_ns
api.add_namespace(user_ns)

from .user.auth import api as auth_ns
api.add_namespace(auth_ns)

# from .author import api as author_ns
# api.add_namespace(author_ns)

# # from .articles import api as article_ns
# # api.add_namespace(article_ns)


# from .product import api as product_ns
# api.add_namespace(product_ns)
