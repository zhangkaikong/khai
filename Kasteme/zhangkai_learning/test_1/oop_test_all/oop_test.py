class Animal(object):
    def __init__(self,name):
        self.name = name

    def run(self):
        print 'Animal is running!'

    def animalRun(self,Animal):
        Animal.run()


class Dog(Animal):
    def run(self):
        print '%s is running!'%(self.name)

class sheep(Animal):
    def run(self):
        print '%s is running!'%(self.name)

dog = Dog('Huski')
animal = Animal('Animal')
sheep = sheep('Porl')
animal.animalRun(dog)
animal.animalRun(sheep)

dog1 = Dog('Tugou')
dog2 = Dog('Gaosheng')
animal.animalRun(dog1)
animal.animalRun(animal)
animal.animalRun(dog2)
