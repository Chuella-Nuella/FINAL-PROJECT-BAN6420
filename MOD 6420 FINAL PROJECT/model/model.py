from pydantic import BaseModel
from typing import Optional

class UserModelCreate(BaseModel):
    name: str
    email: str
    age: int

class UserModelUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
import pydantic 
print(pydantic.__version__)
