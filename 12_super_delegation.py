# class Person:
#     def __init__(self, name) -> None:
#         self.name = name

# class Student(Person):
#     def __init__(self, name, surname) -> None:
#         super().__init__(name)
#         self.surname = surname


class Person:
    def hello(self):
        print(f"Bonus with {self}")

class Student(Person):
    def hello(self):
        print("Student obj.hello() is called")
        super().hello()



s = Student()

print(s.__dict__)

s.hello()

print(hex(id(s)))



