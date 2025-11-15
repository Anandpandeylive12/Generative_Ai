class Car:
    def __init__(self,brand , model ):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand
    
    def fullName(self):
        return f"{self.brand} {self.model}"

#inherting the class
class ElectricCar(Car):
    def __init__(self, brand , model , battery_size):
        super().__init__(brand , model)
        self.battery_size  = battery_size

my_tesla = ElectricCar("Tesla","Model S", "85kWh")
print(my_tesla.model)
print(my_tesla.brand)
print (my_tesla.get_brand())
print(my_tesla.battery_size)
print(my_tesla.fullName())

       

    

my_car = Car("Toyota","corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.fullName())

my_new_car = Car("Tata","Safari")
print(my_new_car.model)
print(my_new_car.fullName())