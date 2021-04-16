from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#API documentation is accessible by /doc or /redoc path
app = FastAPI()

@app.post('/survey')
def survey():
    return {'status':'survey ok'}

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/sentences')
def get_test_data():
    return {'sentences': [
        'Sample 1 sentence',
        'Sample 2 sentence',
        'Sample 3 sentence',
        'Sample 4 sentence',
        'Sample 5 sentence',
    ]}

@app.post('/test-data')
def test_data():
    return {'status': 'test-data ok'}

@app.get('/statistics')
def show_statistics():
    return {'status':'statistics ok'}