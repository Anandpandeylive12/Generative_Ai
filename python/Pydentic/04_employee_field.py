from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name:str = Field(..., min_length=2, max_length=50, description="Employee's full name",examples ="Hitesh Chaudhary")
    department:Optional[str] = 'General'
    salary:float = Field(..., gt=10000, description="Employee's monthly salary", examples=50000.00)
    

class user(BaseModel):
    email:str = Field(...,regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', description="User's email address", examples="hitesh@company.com")
    phone:str = Field(...,regex=r'^\+?[1-9]\d{1,14}$', description="User's phone number", examples="+1234567890")
    