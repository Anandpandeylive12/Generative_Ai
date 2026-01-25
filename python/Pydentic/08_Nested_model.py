from typing import List , Optional
from pydantic import BaseModel, Field

class Address(BaseModel):
    street: str = Field(..., description="Street address", examples="123 Main St")
    city: str = Field(..., description="City name", examples="New York")
    state: str = Field(..., description="State name", examples="NY")
    zip_code: str = Field(..., description="ZIP code", examples="10001")
    
class User(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50, description="User's full name", examples="Anand Pandey")
    address: Address
    
address = Address(
    street = '123 Main St',
    city = 'New York',
    zip_code = '10001',
    state = 'NY'
)
user = User(
    id = 1, 
    name = 'Anand Pandey',
    address = address
)