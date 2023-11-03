from fastapi import FastAPI

# The app variable is the main point of interaction to create the API
app = FastAPI()

# Associate root path with read_root() by registering it in FastAPI. FastAPI listens to the root path and delegates all incoming GET requests to your read_root() function.
@app.get("/")
def read_root():
    # This string is displayed when you send a request to the root path of your API.
    return "Hello World!! This is an API!!!"