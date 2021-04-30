from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, status
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from . import schemas, controller, database, models

#API documentation is accessible by /doc or /redoc path
app = FastAPI()


#Whenever we find some find any model we will create it on db
models.Base.metadata.create_all(database.engine)

get_db = database.get_db

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/survey', status_code = status.HTTP_201_CREATED)
def survey(request: schemas.survey, db: Session = Depends(get_db)):
    controller.add_survey(request, db)
    return {'status': 'test-data ok'}

@app.get('/sentences')
def get_test_data():
    return {'sentences': [
        'Wylej na patelnię tylko tyle ciasta, by masa przykryła powierzchnię patelni.',
        'Tutaj może Ci się przydać płaska łopatka do przewracania naleśników.',
        'Zabezpiecz wąż, aby nie przemieszczał się podczas pracy urządzenia.',
        'Wciśnij przycisk „WIROWANIE” taką ilość razy, aby wybrać żądaną ilość obrotów.',
        'Wśród gimnazjalistów przeprowadzono ankietę na temat ich zainteresowań',
        'Ilu uczniów brało udział w corocznej ankiecie?',
        'Jeśli wejdziesz między wrony, musisz krakać tak jak one.',
        'Lepszy w domu groch, kapusta niż na wojnie kura tłusta.',
        'W 966 roku książę Mieszko I przyjął chrzest i zapoczątkowało to chrystianizację kraju.',
        '18 kwietnia 1025 roku w Gnieźnie odbyła się koronacja Bolesława Chrobrego na króla Polski.'
    ]}

@app.post('/test-data', status_code = status.HTTP_201_CREATED)
def test_data(request: List[List[schemas.keystroke]]):
    controller.add_test_data(request)
    return {'status': 'test-data ok'}

@app.get('/statistics')
def show_statistics():
    return {'status':'statistics ok'}