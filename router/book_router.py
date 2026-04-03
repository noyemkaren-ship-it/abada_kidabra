from fastapi import APIRouter
from services.books_services import *
from schemas.book import BookCreate
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from fastapi import Request

limiter = Limiter(key_func=get_remote_address)

book_router = APIRouter()

@book_router.post("/book", tags=["book_CRUD"])
@limiter.limit("5/minute")
async def create_book_now(request: Request, book: BookCreate):
    result = create_book(name=book.name, yer=book.yer, author=book.author, price=book.price, category=book.category)
    return result

@book_router.get("/books", tags=["book_CRUD"])
async def get_books():
    result = get_all_books()
    return result

@book_router.delete("/book/{id}", tags=["book_CRUD"])
@limiter.limit("5/minute")
async def delete_book(request: Request, id: int):
    result = delete_book_by_id(id)
    return result

@book_router.patch("/book/{id}", tags=["book_CRUD"])
@limiter.limit("5/minute")
async def patch_book(request: Request, id: int, book: BookCreate):
    result = patch_book_by_id(id, name=book.name, yer=book.yer, author=book.author, price=book.price, category=book.category)
    return result


@book_router.get("/search?book/{name}", tags=["book_CRUD"])
async def get_book_by_name_now(name: str):
    result = get_book_by_name(name)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Book not found")

@book_router.get("/books/sort/{category}", tags=["book_CRUD"])
async def get_books_by_category(category: str):
    result = get_all_books_by_category(category)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Books not found")
