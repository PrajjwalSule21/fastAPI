from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': "title one", 'author': 'author one', 'category':'science'},
    {'title': "title two", 'author': 'author two', 'category':'science'},
    {'title': "title three", 'author': 'author three', 'category':'history'},
    {'title': "title four", 'author': 'author four', 'category':'math'},
    {'title': "title five", 'author': 'author five', 'category':'math'},
    {'title': "title six", 'author': 'author six', 'category':'math'}
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


