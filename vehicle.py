class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print(self.year, self.make, self.model)

car = Vehicle("Toyota", "Land Cruiser", "2000")
car.print_info()