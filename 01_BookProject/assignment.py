"""
Here is your opportunity to keep learning!

1. Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.

Solution in next video
"""
from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': "title one", 'author': 'Prajjwal', 'category':'science'},
    {'title': "title two", 'author': 'Manoj', 'category':'science'},
    {'title': "title three", 'author': 'Hardik', 'category':'history'},
    {'title': "title four", 'author': 'John', 'category':'math'},
    {'title': "title five", 'author': 'Prajjwal', 'category':'math'},
    {'title': "title six", 'author': 'Sujal', 'category':'math'},
    {'title': "title seven", 'author': 'Prajjwal', 'category':'history'}

]

# by path parameter
@app.get("/books/{author}")
def get_book_by_path(author: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            book_to_return.append(book)
    return book_to_return


# by query parameter
@app.get("/books/")
def get_book_by_query(author: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            book_to_return.append(book)
    return book_to_return



