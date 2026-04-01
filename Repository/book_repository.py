from models.book import Book
from database.Base import session



class BookRepository:
    
    def create_book(self, name: str, yer: int, author: str, price: int, category: str):
        book = Book(name=name, yer=yer, author=author, price=price, category=category)
        session.add(book)
        session.commit()
        return book
    
    def get_all_books(self):
        books = session.query(Book).all()
        return books
    
    def get_all_books_by_category(self, category: str):
        books = session.query(Book).filter(Book.category == category).all()
        return books
    
    
    def get_book_by_id(self, id: int):
        book = session.query(Book).filter(Book.id == id).first()
        return book
    
    def delete_book_by_id(self, id: int):
        book = session.query(Book).filter(Book.id == id).first()
        if book:
            session.delete(book)
            session.commit()
            return book
        return None
    
    def update_book_by_id(self, id: int, **kwargs):
        book = self.get_book_by_id(id)
        if not book:
            return None
        
        for key, value in kwargs.items():
            if hasattr(book, key):
                setattr(book, key, value)
        
        session.commit()
        return book
    
    def get_book_by_name(self, name: str):
        book = session.query(Book).filter(Book.name == name).first()
        return book
    

        
    
