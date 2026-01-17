from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool = True
    
Product_one = Product(id=1, name="Laptop", price=999.99 , in_stock=True)
Product_two = Product(id=2, name="Smartphone", price=499.49)  
Product_three = Product(id=3, name="Headphones", price=199.99, in_stock=False)  

print(Product_one, "\n", Product_two , "\n", Product_three)



    
    