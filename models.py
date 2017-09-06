from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///boards.db')
session = sessionmaker(bind=engine)()



class Board(Base):

    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True)
    layout = Column(String(100), nullable=False)
    name = Column(String(50), nullable=False)
