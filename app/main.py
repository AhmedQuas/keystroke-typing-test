from fastapi import FastAPI

#API documentation is accessible by /doc or /redoc path
app = FastAPI()

@app.get('/statistics')
def show_statistics():
    return {'status':'statistics ok'}

@app.post('/survey')
def survey():
    return {'status':'survey ok'}


@app.post('/test-data')
def test_data():
    return {'status': 'test-data ok'}
