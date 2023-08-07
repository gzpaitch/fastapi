from fastapi import FastAPI
from newsapi import NewsApiClient
import os
import requests

app = FastAPI()

newsapi = NewsApiClient(api_key=os.getenv('60091c54ad7643aa9663e0505e724c31'))

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/news")
async def get_news():
    response = requests.get('https://newsapi.org/v2/everything?q=mercado+imobiliário&from=2023-07-30&to=2023-08-06&language=pt&sortBy=publishedAt&pageSize=40&page=2&apiKey=60091c54ad7643aa9663e0505e724c31')
    return response.json()

@app.get("/top-headlines")
async def get_top_headlines():
    top_headlines = newsapi.get_top_headlines(q='mercado imobiliario',
                                          category='business',
                                          language='pt',
                                          country='br')
    return top_headlines

@app.get("/everything")
async def get_everything():
    all_articles = newsapi.get_everything(q='mercado imobiliario',
                                      language='pt',
                                      sort_by='relevancy')
    return all_articles

@app.get("/sources")
async def get_sources():
    sources = newsapi.get_sources(language='pt', country='br')
    return sources

# 
# 
# from fastapi import FastAPI
# import requests

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

# @app.get("/news")
# async def get_news():
#     response = requests.get('https://newsapi.org/v2/everything?q=mercado+imobiliario&apiKey=60091c54ad7643aa9663e0505e724c31')
#     return response.json()
# 
# 
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}
