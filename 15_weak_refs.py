from weakref import WeakKeyDictionary

# class Person:
#     def __init__(self, name):
#        self.name = name
#     def __eq__(self,obj):
#         return isintance(obj, Person) and self.name == obj.name
#     def __hash__(self) -> int:
#         return hash(self.name)
    
# p = Person("Ivan")

# print(hash(p))


class IntDescriptor:
    def __init__(self) -> None:
        self._values = WeakKeyDictionary()

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

print(hex(id(v1)))

v1.x = 10

print(Vector.x._values.keyrefs())

del v1 

print(Vector.x._values.keyrefs())