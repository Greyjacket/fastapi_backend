from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {"name": "Alex"}}

@app.get('/about')
def about():
    return {'data': {"name": "Alex"}}