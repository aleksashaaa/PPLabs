#1
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

#2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1)

#3 __str__ - return values
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

#4
class Person:
    def __init__(self, name, age):  #it can be not only self
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#5 modify objects
p1.age = 40
print(p1.age)

#6 deleting objects
del p1.age