from sqlalchemy import create_engine, Column, Integer, String
from database.Base import Base


class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
