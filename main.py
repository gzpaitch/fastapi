from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/news")
async def get_news():
    response = requests.get('https://newsapi.org/v2/everything?q=mercado+imobiliario&apiKey=60091c54ad7643aa9663e0505e724c31')
    return response.json()


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}
