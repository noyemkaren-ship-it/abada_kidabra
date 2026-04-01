from fastapi import APIRouter, HTTPException
from services.category_services import get_all_categories, create_category, delete_category_by_id
from schemas.category import CategoryCreate


cat_router = APIRouter()

@cat_router.get("/categories", tags=["category_CRUD"])
async def get_categories():
    result = get_all_categories()
    return result

@cat_router.post("/categories", tags=["category_CRUD"])
async def create_category_create(category: CategoryCreate):
    result = create_category(category.name)
    return result


@cat_router.delete("/categories/{id}", tags=["category_CRUD"])
async def delete_category(id: int):
    result = delete_category_by_id(id=id)
    if result:
        return {"message": "Category deleted"}
    raise HTTPException(status_code=404, detail="Category not found")