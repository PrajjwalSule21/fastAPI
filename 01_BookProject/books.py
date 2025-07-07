from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': "title one", 'author': 'author one', 'category':'science'},
    {'title': "title two", 'author': 'author two', 'category':'science'},
    {'title': "title three", 'author': 'author three', 'category':'history'},
    {'title': "title four", 'author': 'author four', 'category':'math'},
    {'title': "title five", 'author': 'author five', 'category':'math'},
    {'title': "title six", 'author': 'author two', 'category':'math'}
]

# @app.get("/")
# async def first_api():
#     return {"message":"Hello Prajjwal!"}
#
#
# @app.get("/second-api-endpoint")
# async def second_api():
#     return {"message":"This is second api endpoint"}


@app.get('/books')
async def read_all_books():
    return BOOKS


# to open swagger ui just right /docs instead of any path like: http://127.0.0.1:8000/docs
# FastAPI have two inbuilt UI to test the developed endpoints:
# -> Swagger UI - /docs (this path open swagger UI)
# -> ReDoc UI - /redoc (this path open ReDoc UI)


"""
Path Parameter: 
1. This are request parameter that have been attached to the URL
2. Path parameter are usually defined as a way to find information based on location.

# Static path parameter -> /books
# dynamic path parameter -> /books/{dynamic_path}

As there no space in apicall (URL) and if we needed one so we have to define with %20
"""


# @app.get("/books/{dynamic_param}")
# async def real_all_books(dynamic_param: str):
#     return {'dynamic_param': dynamic_param}


# @app.get("/books/mybook")
# async def real_all_books():
#     """
#     This api will return
#     {
#       "dynamic_param": "mybook"
#     }
#
#     instead of
#     {
#       "Book_title": "My favorite book!"
#     }
#
#     Because FastAPI works in chronological manner so order matter for defining the apis
#
#     """
#     return {'Book_title': "My favorite book!"}

@app.get("/books/{book_title}")
async def real_all_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold(): #casefold() will lowercase the string
            return book
    return None


"""
Query Parameters

- Query parameter are request parameters that have been attached after a '?'
- Query parameter have name=value pairs ex: 127.0.0.1:8000/books/?category=math
"""

@app.get("/books/") #fastapi will automatically define after / there will be query param
async def read_category_by_query(category: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            book_to_return.append(book)
    return book_to_return


# we can use query param with path param as well
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            book_to_return.append(book)
    return  book_to_return


"""
POST request method

- used to create data
- POST can have a body that have additional information that GET does not have.
"""

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
