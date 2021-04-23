from fastapi import FastAPI, status
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from . import schemas
from . import controller

#API documentation is accessible by /doc or /redoc path
app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/survey', status_code = status.HTTP_201_CREATED)
def survey(request: schemas.survey):
    controller.add_survey(request)
    return {'status': 'test-data ok'}

@app.get('/sentences')
def get_test_data():
    return {'sentences': [
        'Sample 1 sentence',
        'Sample 2 sentence',
        'Sample 3 sentence',
        'Sample 4 sentence',
        'Sample 5 sentence',
    ]}

@app.post('/test-data', status_code = status.HTTP_201_CREATED)
def test_data(request: List[List[schemas.test_data]]):
    controller.add_test_data(request)
    return {'status': 'test-data ok'}

@app.get('/statistics')
def show_statistics():
    return {'status':'statistics ok'}