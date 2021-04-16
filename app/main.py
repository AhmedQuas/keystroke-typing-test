from fastapi import FastAPI

#API documentation is accessible by /doc or /redoc path
app = FastAPI()

@app.get('/')
def index():
    return {'status':'ok'}
