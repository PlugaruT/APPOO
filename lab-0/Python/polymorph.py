'''
    Polymorphism demonstration in Python
'''

class Animal(object):
    def Name(self):
        pass
    def Sleep(self):
        print 'sleep'
    def MakeNoise(self):
        pass

class Dog(Animal):
    def Name(self):
        print 'I am dog'
    def MakeNoise(self):
        print 'Ham Ham :)'

class Cat(Animal):
    def Name(self):
        print 'I am cat'
    def MakeNoise(self):
        print 'Mew Mew :)'

class Lion(Animal):
    def Name(self):
        print 'I am lion'
    def MakeNoise(self):
        print 'Arr Arr :)'

class TestAnimals:
    def PrintName(self, animal):
        animal.Name()
    def GoSleep(self, animal):
        animal.Sleep()
    def MakeNoise(self, animal):
        animal.MakeNoise()



animal = TestAnimals()
dog = Dog()
cat = Cat()
lion = Lion()

animal.PrintName(dog)
animal.GoSleep(dog)
animal.MakeNoise(dog)
animal.PrintName(cat)
animal.GoSleep(cat)
animal.MakeNoise(cat)
animal.PrintName(lion)
animal.GoSleep(lion)
animal.MakeNoise(lion)
