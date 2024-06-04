import hashlib

a = "OLEG"

# print(a)
# print(hashlib.md5(a.encode('utf8')).hexdigest()) 

# print(hash("1"))
# print(hash(1))

class Person:
    def __init__(self, name):
        self._name = name

        @property
        def name(self):
            return self._name
        
        def __hash__(self):
            return hash(self.name)
        
        def __eq__(self, person_obj):
            return isinstance(person_obj, Person) and self.name == person_obj.name
        
p1 = Person('Ivan')
p2 = Person('Ivan')

p3 = Person("Oleg")
print(p1)
print(p2)

print(p1 == p2)

print(hash(p1))
print(hash(p2))


d = {p1: "Ivaankv Ivan"}

print(d.get(p1))
