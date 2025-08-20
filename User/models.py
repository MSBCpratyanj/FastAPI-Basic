from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

class Role(str,Enum):
    ADMIN = 'admin'
    USER = "user"
    
class Gender(str,Enum):
    MALE = 'male'
    FEMALE = 'female'
    
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    email:str
    psw:str
    gender:Gender
    roles: List[Role]
    created_at: datetime
    
class Show_user(BaseModel):
    id:int 
    name:str
    email:str