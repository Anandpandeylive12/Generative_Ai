from pydantic import BaseModel, Field, ConfigDict
from typing import List
from datetime import datetime, timezone

class Address(BaseModel):
    street: str = Field(..., description="Street address", examples=["123 Main St"])
    city: str = Field(..., description="City name", examples=["New York"])
    state: str = Field(..., description="State name", examples=["NY"])
    zip_code: str = Field(..., description="ZIP code", examples=["10001"])
    
class User(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50, description="User's full name")
    address: Address
    email: str = Field(..., description="User's email address")
    is_active: bool = Field(default=True, description="Is the user active?")
    # Using timezone-aware UTC now
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), 
        description="Account creation time"
    )
    tags: List[str] = []
    
    # In Pydantic V2, simple ISO format is the default. 
    # Extra config is usually only needed for complex serialization.
    model_config = ConfigDict(populate_by_name=True)

# 1. Create the Address instance
user_address = Address(
    street='123 Main St',
    city='New York',
    state='NY',
    zip_code='10001'
)

# 2. Create the User instance
user = User(
    id=1,
    name='Anand Pandey',
    address=user_address,
    email='anand.pandey@example.com',
    created_at=datetime(2023, 10, 5, 14, 48, tzinfo=timezone.utc),
    tags=['admin', 'user']
)

# 3. Convert to Dictionary
python_dict = user.model_dump()

print("Python Dictionary Representation:")
print(python_dict)

# 4. Convert to JSON (to see the formatted datetime)
print("\nJSON Representation:")
print(user.model_dump_json(indent=2))