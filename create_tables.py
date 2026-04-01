# init_db.py
from database.Base import engine, Base
from models.book import Book
from models.category import Category

# Create all tables
Base.metadata.create_all(bind=engine)
print("Database tables created successfully!")