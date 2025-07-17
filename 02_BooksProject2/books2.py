from fastapi import FastAPI, Body

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

BOOKS = [
    Book(1, "Computer Science", "Prajjwal", "Great Book on computer sceince", 5),
    Book(2, "FastAPI DEV", "Prajjwal", "Nice Book", 5),
    Book(3, "JavaScript for Beginner", "Harsh", "Awesome book", 4),
    Book(4, "C++", "Sujal", "Great Book", 5),
    Book(5, "C Language", "Vaidik", "Nice Read", 4),
]


@app.get("/books")
async def real_all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request=Body()):
    BOOKS.append(book_request)