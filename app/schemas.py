from pydantic import BaseModel

class test_data(BaseModel):
    key: str
    downTimeStamp: int
    upTimeStamp: int
    repeat: bool
    shiftKey: bool
