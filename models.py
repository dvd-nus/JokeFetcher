# models.py
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./jokes.db"  # SQLite database

Base = declarative_base()

class Joke(Base):
    __tablename__ = 'jokes'
    
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    joke_type = Column(String)
    joke = Column(String, nullable=True)
    setup = Column(String, nullable=True)
    delivery = Column(String, nullable=True)
    nsfw = Column(Boolean, default=False)
    political = Column(Boolean, default=False)
    sexist = Column(Boolean, default=False)
    safe = Column(Boolean, default=True)
    lang = Column(String, default='en')

# Create a database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create all tables
Base.metadata.create_all(bind=engine)

# SessionLocal to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
