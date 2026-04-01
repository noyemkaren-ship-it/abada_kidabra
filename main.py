from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from router.book_router import book_router
from router.category_router import cat_router
from services.books_services import get_all_books


app = FastAPI(
    docs_url="/secret-docs-2025",
    redoc_url="/secret-redoc-2025"
)
app.include_router(book_router)
app.include_router(cat_router)
templates = Jinja2Templates(directory="templates")


@app.middleware("http")
async def add_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response

@app.get("/", tags=["page"])
async def root():
    return {"message": "Hello World"}

@app.get("/books/page", tags=["page"])
async def get_books(request: Request):
    books = get_all_books()
    return templates.TemplateResponse("index.html", {"request": request, "books": books})