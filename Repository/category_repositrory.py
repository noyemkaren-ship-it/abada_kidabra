from models.category import Category
from database.Base import session



class CategoryRepository:
    
    def create_category(self, name: str):
        category = Category(name=name)
        session.add(category)
        session.commit()
        return category
    
    def get_all_categories(self):
        categories = session.query(Category).all()
        return categories
    
    def get_category_by_name(self, name: str):
        category = session.query(Category).filter(Category.name == name).first()
        return category
    
    def delete_category_by_id(self, id: int):
        category = session.query(Category).filter(Category.id == id).first()
        if category:
            session.delete(category)
            session.commit()
            return category
        return None
    
    

