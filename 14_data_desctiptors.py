from time import time
from random import choice
import ctypes
import sys


# class Epoch:
#     def __get__(self, instance, owner_class):
#         print(f'id of self: {id(self)}')
#         if instance is None:
#             return self
#         # print(f'Self: {self}')
#         # print(f'Instance: {instance}')
#         # print(f'Owner class: {owner_class}')
#         return int(time())
    
#     def __set__(self, instance, value):
        # pass
    
# class MyTime:
#     epoch = Epoch()

# m = MyTime()
# m1 = MyTime()

# m.epoch
# print(m.epoch)
# m1.epoch
# print(m1.epoch)

# MyTime.epoch


# !!!!
class IntDescriptor:
    def __init__(self) -> None:
        self._values = {}

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance)

class Vector:
    x = IntDescriptor()
    y = IntDescriptor()

v1 = Vector()
v1.x = 5
v1.y = 10

v2 = Vector()
v2.x = 200
v2.y = 1000

print(v1.x)
print(v2.x)

print(Vector.x._values)


v = 1
val = 'oleg'

print(sys.getrefcount(v))
print(sys.getrefcount(val))

def ref_count(obj_id):
    return ctypes.c_long.from_address(obj_id).value

# ref_count(val)
print(ref_count(id(val)))

print(ref_count(id(v1)))
print(ref_count(id(v2)))

v3 = Vector()

print(ref_count(id(v3)))

id_v = id(v3)

v3.x = 30

print(ref_count(id(v3)))

v3.y = 50

print(ref_count(id(v3)))

del v 

print(ref_count(id(v3)))

print(Vector.x._values.keys())
print(list(Vector.x._values.keys())[0])


 