from pydantic import BaseModel, field_validator

class Person(BaseModel):
    first_name: str
    last_name: str
    
    @field_validator('first_name', 'last_name')
    def names_must_be_capitalized(cls, v):
        if not v.istitle():
            raise ValueError('Names must be capitalized')
        return v
    
    
class Account(BaseModel):
    account_number: str
    balance: float

    @field_validator('account_number', mode='before' )
    def account_number_must_be_numeric(cls, v):
        if not v.isdigit():
            raise ValueError('Account number must be numeric')
        return v