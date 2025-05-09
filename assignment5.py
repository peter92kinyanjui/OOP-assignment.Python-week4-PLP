# Assignment 5: Classes and Objects
class vehicle:
    def __init__(self, model, color, year, price):
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        return f"Vehicle details: \nmodel= {self.model} \ncolor= {self.color} \nyear= {self.year} \nprice= {self.price})"
    
    def carMove(self):
        print("Drving... 🚗")
        
    def planeMove(self):
        print("Flying... ✈️")
        
    def boatMove(self):
        print("Sailing... ⛵")      
        
        
        
        
# Creating objects of the vehicle class
# and calling their methods
#A car
car1 = vehicle("Toyota", "Red", 2020, 20000)
print(car1)
print(car1.carMove())

#A plane
plane1 = vehicle("Boeing", "White", 2015, 5000000)
print(plane1)
print(plane1.planeMove())

#A boat
boat1 = vehicle("Yacht", "Blue", 2018, 300000)
print(boat1)
print(boat1.boatMove())







