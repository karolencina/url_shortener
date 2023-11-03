import validators
from fastapi import FastAPI, HTTPException

from . import schemas

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)

# The app variable is the main point of interaction to create the API
app = FastAPI()

# define the create_url endpoint, which expects a URL string as a POST request body
@app.post("/url")
def create_url(url: schemas.URLBase):
    if not validators.url(url.target_url):
        raise_bad_request(message="The provided URL is not valid.")
    return f"TODO: Create database entry for: {url.target_url}"