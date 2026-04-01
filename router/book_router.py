from fastapi import APIRouter
from services.books_services import *
from schemas.book import BookCreate


book_router = APIRouter()

@book_router.post("/book")
async def create_book_now(book: BookCreate):
    result = create_book(name=book.name, yer=book.yer, author=book.author, price=book.price, category=book.category)
    return result

@book_router.get("/books")
async def get_books():
    result = get_all_books()
    return result

@book_router.delete("/book/{id}")
async def delete_book(id: int):
    result = delete_book_by_id(id)
    return result

@book_router.patch("/book/{id}")
async def patch_book(id: int, book: BookCreate):
    result = patch_book_by_id(id, name=book.name, yer=book.yer, author=book.author, price=book.price, category=book.category)
    return result


@book_router.get("/search?book/{name}")
async def get_book_by_name_now(name: str):
    result = get_book_by_name(name)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Book not found")

@book_router.get("/books/sort/{category}")
async def get_books_by_category(category: str):
    result = get_all_books_by_category(category)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Books not found")
