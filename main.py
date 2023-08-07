from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/news")
async def get_news():
    response = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY')
    return response.json()


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}
