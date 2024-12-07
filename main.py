# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Joke, SessionLocal, engine
from joke_fetcher import fetch_jokes

# Initialize FastAPI app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to fetch jokes and store them in the database
@app.post("/fetch_jokes")
async def fetch_and_store_jokes(num_jokes: int = 100, db: Session = Depends(get_db)):
    jokes = fetch_jokes(num_jokes)
    for joke_data in jokes:
        joke = Joke(**joke_data)
        db.add(joke)
    db.commit()
    return {"message": f"{num_jokes} jokes fetched and stored in the database!", "jokes": jokes}

# Endpoint to get all jokes
@app.get("/jokes")
def get_jokes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    jokes = db.query(Joke).offset(skip).limit(limit).all()
    return jokes
