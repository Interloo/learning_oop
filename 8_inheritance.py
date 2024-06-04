# class Person:
#     adg = 0
#     def hello(self):
#         print("Hello")

# class Student(Person):
#     pass

# s = Student()


# # print(s.__dict__)
# print(dir(s))

# print(s.adg)
# s.hello()

# print(s.__dict__)

# print(Student.__dict__)

# print(Person.__dict__)

# print(object.__dict__)



# !!!!

# class IntelCpu:
#     cpu_socket = 1151
#     name = "Intel"

# class I7(IntelCpu):
#     pass

# class I5(IntelCpu):
#     pass


# i5 = I5()
# i7 = I7()

# print(isinstance(i5, IntelCpu))

# print(type(i5))

# print(issubclass(I5, IntelCpu))


# class One:
#     pass

# class Two(One):
#     pass

# class Three(Two):
#     pass

# print(issubclass(Three, One))

# print(isinstance(i5, type(i7)))

# print(issubclass(type(i5), type(i7)))


# !!!
# class Person:
#     def hello(self):
#         print("I am Person")

# class Student(Person):
#     def goodbye(self):
#         print("Goodbye")



# s = Student()

# s.hello()
# s.goodbye()

# print(s.__dict__)

# print(Student.__dict__)

# print(Person.__dict__)



class Person:
    def __init__(self, name) -> None:
        self.name = name

    def hello(self):
        print(f"Hello from {self.name}")

class Student(Person):
    pass

s = Student("Ivan")

s.hello()

print(s.__dict__)