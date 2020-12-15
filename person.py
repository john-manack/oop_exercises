class Person:
    species = "homosapien"
    legs = 2
    eyes = 2
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def print_contact_info(self):
        print("%s's email: %s" % (self.name, self.email))
        print("%s's phone number: %s" % (self.name, self.phone))

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

sonny.print_contact_info()
jordan.print_contact_info()

sonny.friends.append(jordan)
jordan.friends.append(sonny)

print(len(sonny.friends))
print(len(jordan.friends))