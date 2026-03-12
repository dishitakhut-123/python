class Vehicle:
    def __init__(self,id,brand,price):
        self.id=id
        self.brand=brand
        self.price=price

    def display(self):
        print("vehicle id",self.id)
        print("vehicle brand",self.brand)
        print("vehicle price",self.price)


class Car(Vehicle):
    def __init__(self,id,brand,price,num_doors,fuel_type):
        super().__init__(id,brand,price)
        self.num_doors=num_doors
        self.fuel_type=fuel_type

    def display(self):
        super().display()   # call parent class method
        print("Doors:", self.num_doors)
        print("Fuel Type:", self.fuel_type)
        print("-----------------")


car1 = Car(201, "Toyota", 800000, 4, "Petrol")
car2 = Car(202, "Honda", 900000, 4, "Diesel")

car1.display()
car2.display()