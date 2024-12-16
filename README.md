# Joke API Fetcher

This project fetches jokes from the [JokeAPI](https://sv443.net/jokeapi/v2/) and stores them in a SQLite database.

## Requirements
- FastAPI
- Uvicorn
- SQLAlchemy
- httpx

## Setup

1. Install the dependencies:
`pip install fastapi uvicorn sqlalchemy httpx`


2. Run the FastAPI app:
`uvicorn main:app --reload`


3. To fetch and store jokes in the db, send a POST request to:
`http://127.0.0.1:8000/fetch_jokes`, which retrieves 100 jokes by default.
To specify the number of jokes to fetch send the POST request to `http://127.0.0.1:8000/fetch_jokes?num_jokes=100`.


4. To retrieve stored jokes, send a GET request to:
`http://127.0.0.1:8000/jokes?skip=0&limit=10`


## Database
The jokes are stored in a SQLite database located in the root directory (jokes.db).
