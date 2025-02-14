
from typing import Any


print(1 + 1)

print("1" + "1")

print(["a"] + ["b"])

print("1".__add__("b"))

class Person:
    age = 1 
    def __add__(self, value):
        self.age += 1 
        return self.age
    
p = Person()

print(p + 123)

print(p + "asdasad")

class Room:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, room_obj):
        if isinstance(room_obj, Room):
            return self.area + room_obj.area
        raise TypeError("Wrong Object")
    
    def  __eq__(self, room_obj):
        if self.area == room_obj.area:
            return True
        return False
    

r1 = Room(3, 5)
r2 = Room(4, 7)

print(r1.area)
print(r2.area)
print(r1 + r2)

print(r1 == r2)

