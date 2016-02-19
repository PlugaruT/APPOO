'''
    Inheritance demonstration in Python
'''

class Person(object):
    def speak(self):
        print 'I can speak'

class Man(Person):
    def laugh(self):
        print 'Ha Ha Ha'

m = Man()
m.speak()
m.laugh()
