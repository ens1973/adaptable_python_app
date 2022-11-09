from .models import Book
from .schemas import book_schema as schema
from .schemas import book_schema_many as schema_many


def create_book(data):
    """Given serialized data, deserialize it and create a new book"""
    book = schema.load(data)
    book.save()
    return schema.dump(book), 201


def get_all_books():
    """Deserialize and return all books in database"""
    return schema_many.dump(Book.objects.all()), 200


def get_book(book_id):
    """Given an book ID, return a serialized book object"""
    if not (book := Book.objects(id=book_id).first()):
        return {"message": f"Book with ID {book_id} does not exist"}, 404

    return schema.dump(book), 200


def update_book(book_id, data):
    if not (book := Book.objects(id=book_id).first()):
        return {"message": f"Book with ID {book_id} does not exist"}, 404

    schema.update(book, data)
    book.save()
    return schema.dump(book), 200


def delete_book(book_id):
    if not (book := Book.objects(id=book_id).first()):
        return {"message": f"Book with ID {book_id} does exist"}, 404

    book.delete()
    return "Done!", 204
