# Lecture 60

class Dog():
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF CLASS
    species = 'mammal'



    def __init__(self, breed, name):
        # Attributes
        # assign it to self.attribute_name
        self.breed = breed
        self.name = name

    #OPERATIONS/ACTIONS - methods

    def bark(self, number):
        print(f'WOOF! My name is {self.name} and the number is {number}')

class Circle():
    pi = 3.14
        
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi

    def get_circumference(self):
        return self.radius * self.pi * 2


my_dog = Dog(breed = 'Lab', name='Sammy')
print(f'My dog is a {my_dog.breed}, its name is {my_dog.name} of species: {my_dog.species}')
my_dog.bark(55)
# print(type(my_dog))

my_circle = Circle(30)

print(f'Circle circumference: {my_circle.get_circumference()}')
print(f'Circle area: {my_circle.area}')

class Animal():

    def __init__(self):
        print('Animal Created')

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

myanimal = Animal()

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    
    def who_am_i(self):
        print('I am a dog')
    
    def eat(self):
        print('I am a dog eating')

    def bark(self):
        print('Woof')

mydog = Dog()       
mydog.who_am_i()
mydog.eat()
mydog.bark()






