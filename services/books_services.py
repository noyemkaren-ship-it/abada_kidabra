from Repository.book_repository import BookRepository
from Repository.category_repositrory import CategoryRepository
from fastapi import HTTPException

book_repo = BookRepository()
cat_repo = CategoryRepository()



def create_book(name: str, yer: int, author: str, price: int, category: str):
    if not cat_repo.get_category_by_name(category):
        raise HTTPException(status_code=404, detail="Category not found")
    result =  book_repo.create_book(name, yer, author, price, category)
    return result

def get_all_books():
    result =  book_repo.get_all_books()
    return result

def delete_book_by_id(id: int):
    result =  book_repo.delete_book_by_id(id)
    return result

def patch_book_by_id(id: int, **kwargs):
    result =  book_repo.update_book_by_id(id, **kwargs)
    return result


def get_book_by_id(id: int):
    result =  book_repo.get_book_by_id(id)
    return result


def get_book_by_name(name: str):
    result =  book_repo.get_book_by_name(name)
    return result


def get_all_books_by_category(category: str):
    if not cat_repo.get_category_by_name(category):
        raise HTTPException(status_code=404, detail="Category not found")
    result =  book_repo.get_all_books_by_category(category)
    return result


            