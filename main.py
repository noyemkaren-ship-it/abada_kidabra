from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from router.book_router import book_router
from router.category_router import cat_router
from services.books_services import get_all_books


app = FastAPI()
app.include_router(book_router)
app.include_router(cat_router)
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/books/page")
async def get_books(request: Request):
    books = get_all_books()
    return templates.TemplateResponse("index.html", {"request": request, "books": books})