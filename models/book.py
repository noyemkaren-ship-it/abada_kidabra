from sqlalchemy import create_engine, Column, Integer, String
from database.Base import Base


class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    yer = Column(Integer)
    author = Column(String)
    price = Column(Integer)
    category = Column(String)
