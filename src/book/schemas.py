from marshmallow import EXCLUDE
from marshmallow_mongoengine import ModelSchema
from .models import Book

class BookSchema(ModelSchema):
    class Meta:
        model = Book
        unknown = EXCLUDE
        load_instance = True

book_schema = BookSchema()
book_schema_many = BookSchema(many=True)