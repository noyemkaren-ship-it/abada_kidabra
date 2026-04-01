from Repository.category_repositrory import CategoryRepository
from fastapi import HTTPException

cat_repo = CategoryRepository()

def get_all_categories():
    result = cat_repo.get_all_categories()
    return result

def create_category(name: str):
    result =  cat_repo.create_category(name)
    return result


def delete_category_by_id(id: int):
    if not cat_repo.get_category_by_id(id):
        raise HTTPException(status_code=404, detail="Category not found")
    result =  cat_repo.delete_category_by_id(id)
    return result

