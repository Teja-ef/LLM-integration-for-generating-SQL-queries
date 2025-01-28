from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List 

# Schema for user creation and update
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Schema for user response
class UserResponse(BaseModel):
    user_id: int
    username: str
    email: EmailStr


# Schema for user creation and update
class TaskCreate(BaseModel):
    ToDo: str
    Status : str
    isExist : bool
    user_id : int

class TaskResponse(BaseModel):
    id: int
    ToDo: str
    CreatedAt: datetime
    Status : str
    isExist : bool
    user_id : int

class UserTaskResponse(BaseModel):
    user_id:int
    username: str
    email : EmailStr
    tasks: List[TaskResponse]
    
    class Config:
        orm_mode = True

