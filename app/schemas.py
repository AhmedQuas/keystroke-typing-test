from pydantic import BaseModel

class test_data(BaseModel):
    key: str
    downTimeStamp: int
    upTimeStamp: int
    repeat: bool
    shiftKey: bool

class survey(BaseModel):
    q1: str
    q2: str
