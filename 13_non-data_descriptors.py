
# class Person:
#     def __init__(self, name, surname):
#         self._name = name
#         self._surname = surname
#         self._full_name = None

#     @property
#     def name(self):
#         return self._name
#     @name.setter
#     def name(self, value):
#         self._name = value
#         self._full_name = None

#     @property
#     def surname(self):
#         return self._surname
#     @surname.setter
#     def surname(self, value):
#         self._surname = value 
#         self._full_name = None
                   

#!!!
# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)

#     def set(self, value):
#         self._value = value

#     def get(self):
#         return self._value

# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)

# p = Person("Oleg", "Ivanov")

# print(p.name.get())
# print(p.surname.get())

from time import time
from random import choice

class Epoch:
    def __get__(self, intance, owner_class):
        return int(time())
    
class MyTime:
    epoch = Epoch()

m = MyTime()

print(m.epoch)

class Dise:
    @property
    def numder(self):
        return choice(range(1,7))
    
d = Dise()

# print(d.numder)

class Choice:
    def __init__(self, *choice) -> None:
        self._choice = choice

    def __get__(self, obj, owner):
        return choice(self._choice)
    

# class Game:
#     @property
#     def rock_paper_scissors(self):
#         return choice(['Rock', 'Paper', 'Scissors'])
    
#     @property
#     def flip(self):
#         return choice(['Heads', 'Tails'])
    
#     @property
#     def dise(self):
#         return choice(range(1,7))
    
class Game:
    dise = Choice(1,2,3,4,5,6)
    flip = Choice('Heads', 'Tails')
    rock_paper_scissors = Choice('Rock', 'Paper', 'Scissors')

d = Game()

print(d.flip)
print(d.dise)
print(d.rock_paper_scissors)
