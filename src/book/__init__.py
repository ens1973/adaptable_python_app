from flask import request
from flask_restx import Namespace
from flask_restx import Resource
from flask_restx import fields
from .services import create_book
from .services import get_all_books
from .services import get_book
from .services import update_book
from .services import delete_book

api = Namespace("books", description="Book related operations !")

book_fields = api.model(
    "Book", {"title": fields.String}
)


class BookList(Resource):
    def get(self):
        """Get a list of books"""
        return get_all_books()

    @api.doc(body=book_fields)
    def post(self):
        """Create a new book"""
        return create_book(request.get_json())


class Book(Resource):
    def get(self, book_id):
        """Get an book by ID"""
        return get_book(book_id)

    @api.doc(body=book_fields)
    def put(self, book_id):
        """Update an book by ID"""
        return update_book(book_id, request.get_json())

    def delete(self, book_id):
        """Delete an book by ID"""
        return delete_book(book_id)


api.add_resource(BookList, "")
api.add_resource(Book, "/<string:book_id>")
