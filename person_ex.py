class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

print(sonny.name, sonny.email, sonny.phone)

print(jordan.name, sonny.email, sonny.phone)

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print(self.year, self.make, self.model)

car = Vehicle("Toyota", "Land Cruiser", "2000")
car.print_info()