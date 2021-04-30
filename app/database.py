from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Provide db credentials same as in .env used for docker-compse
db_url = 'mysql+pymysql://{user}:{passwd}@{db_host}/{dbname}?charset=utf8mb4'.format(
    user='',
    passwd='',
    db_host='',
    dbname=''
    )

engine = create_engine(db_url)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()