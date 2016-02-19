'''
    Encapsulation demonstration in Python
'''

class Person(object):
    def __init__(self):
        self.Name = "Tudor" # public attribute
        self.__Surname = "Plugaru" # private atribute

    def PrintNameSurname(self):
        print self.Name + " " + self.__Surname

p = Person()
print p.Name # should be "Tudor"
#print p.__Surname # error! no such attribute
p.PrintNameSurname() # should print name + surname
