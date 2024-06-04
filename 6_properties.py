
class Person:
    def __init__(self, name) -> None:
        self._name = name

    def get_name(self):
        print("From get_name()")
        return self._name
    def set_name(self, value):
        print("From set_name()")
        self._name = value
    # 1
    # name = property(fget=get_name, fset=set_name)
    # 2
    # name = property()
    # name = name.getter(get_name)
    # name = name.setter(set_name)
    # 3
    # name = property(get_name, set_name)
    # 4
    # def name(self):
    #     return self._name
    # name = property(name)
    # 5
    # @property
    # def name(self):
    #     return self._name
    
    # def set_name(self, value):
    #     self._name = value
    # name = name.setter(set_name)
    
    # 6
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    



p = Person("dima")
print(p.name)

print(p.__dict__)

p.name = "Ivan"

print(p.name)

print(p.__dict__)


