class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')

class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says woof!"

class Cat(Animal):

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says meow!"


niko = Dog('niko')
felix = Cat('felix')
#print(niko.speak())
#print(felix.speak())

for pet in [niko, felix]:
    #print(type(pet.speak()))
    print(pet.speak())

