from pydantic import BaseModel
from typing import List , Dict, Optional


class Cart(BaseModel):
    user_id: int
    items:List[str]
    quantity:Dict[str, int]
    
class Blog_post(BaseModel):
    tittle:str
    content:str
    image_url:Optional[str] = None
    
cart_data = {
    "user_id":1,
    "items":["Laptop", "Mouse"],
    "quantity":{"Laptop":1, "Mouse":2} 
}
    
print(Cart(**cart_data))
# print(Blog_post(tittle="My first blog", content="This is the content of my first blog."))
    
