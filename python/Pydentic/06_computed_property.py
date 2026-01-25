from pydantic import BaseModel, computed_field


class Product(BaseModel):
    price: float
    quantity:int
    
    @computed_field
    @property
    def total_field(self)-> float:
        return self.price * self.quantity
    
    
class Booking(BaseModel):
    check_in: str
    check_out: str
    total_price: float

    @computed_field
    @property
    def duration(self) -> int:
        return (self.check_out - self.check_in).days