
# name = "ivan"

# class Person:
#     name = "dima"
    
#     @classmethod
#     def change_name(cls, name):
#         # print(self.name)
#         cls.name = name 

# p = Person()
# # p.print_name()

# print(p.__dict__)
# p.change_name("vasay")

# p.name = "roma"
# print("Instance dict: ", p.__dict__)

# print("Person.name: ", Person.name)


class Person:
    def __init__(self, name) -> None:
        self.name = name

    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            name = f.read().strip()
        return cls(name=name)
    
    @classmethod
    def from_obj(cls, obj):
        if hasattr(obj, "name"):
            name = getattr(obj, "name")
            return cls(name=name)
        return cls
        

p = Person("oleg")
print(p.__dict__)
print(p.name)

p = Person.from_file('text')
print(p.name)

class Config:
    name = "Igor"

p = Person.from_obj(Config)

print(p.name)