from pydantic import BaseModel
import json

class keystroke(BaseModel):
    key: str
    downTimeStamp: int
    upTimeStamp: int
    repeat: bool
    shiftKey: bool

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=0)

class survey(BaseModel):
    q1: str
    q2: str
