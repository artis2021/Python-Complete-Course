class Car:
    # brand = None
    # model = None
    total_car = 0
    def __init__(self, user_brand, user_model):
        self.__brand = user_brand
        self.__model = user_model
        Car.total_car += 1
        
    def fullname(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or deisel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    
    @property
    def model(self):
        return self.__model
            
            
            
        
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        self.batterySize = batterySize
        super().__init__(brand, model)
        
     
    def fuel_type(self):
        return "Electric charge"   
        
        
        


    
# my_Car = Car("Toyota", "Corolla")   
# print(my_Car.brand, my_Car.model) 
# print(my_Car.fullname())

# my_Car1 = Car("TATA", "Safari")
# print(my_Car1.model)

# my_tesla = ElectricCar("Tesla", "Model S", "85 kws")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))



# print(my_tesla.brand)
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

# safari = Car("Tata", "Safari")
# safari.model = "City"
# print(safari.model)
# safari1 = Car("Tata", "Safari")
# print(safari.fuel_type())
# print(Car.total_car)

# print(safari.general_description())
# print(Car.general_description())


class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCar2(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar2("Tesla", "model")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
