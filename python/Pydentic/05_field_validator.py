from pydantic import BaseModel, field_validator, Field

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, description="The user's username", examples="john_doe")
    age: int = Field(..., gt=0, lt=150, description="The user's age", examples=30)

    @field_validator('username')
    def username_must_be_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v