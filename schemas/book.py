from pydantic import BaseModel

class BookCreate(BaseModel):
    name: str
    author: str
    yer: int
    price: int
    category: str

