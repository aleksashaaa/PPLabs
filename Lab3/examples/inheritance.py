#1
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person): #Child of person
    pass

x = Student("Mike", "Olsen")
x.printname()

#2
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname) #to save the inheritance or we can use super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#3
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()