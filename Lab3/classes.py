#1
class String:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("String: ")

    def printString(self):
        print(self.s.upper())

func = String()
func.getString()
func.printString()
print('-----')

#2
class Shape:
    def area(self):
        print("Area of the shape(default): 0")

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        area = self.length ** 2
        print("Area of the square:", area)

shape = Shape()
shape.area() 
n = int(input())
square = Square(n)
square.area()
print('-----')

#3
class Rectangle(Shape):
    def __init__(self, lenght, width):
        super().__init__()
        self.lenght = lenght
        self.width = width

    def area(self):
        print("Area of the Rectangle:", self.lenght * self.width)

l = int(input("Lenght:"))
w = int(input("Width:"))
rect = Rectangle(l, w)
rect.area()
print('-----')

#4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, nx, ny):
        self.x = nx
        self.y = ny

    def dist(self, point2):
        dx = self.x - point2.x
        dy = self.y - point2.y
        print((dx**2 + dy**2)**(1/2))

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
p1 = Point(x1, y1)
p2 = Point(x2, y2)
print("Point1:")
p1.show()
print("Point2:")
p2.show()
p1.move(1, 3)
print("Point1 after change:")
p1.show()
print("Distance:")
p1.dist(p2)
print('-----')

#5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        money = float(input("Add money: "))
        self.balance += money

    def withdraw(self):
        money = float(input("Withdraw money: "))
        if money > self.balance:
            print("You have", self.balance, "$. We will withdraw all money")
            self.balance -= money
            self.balance = 0
        else:
            self.balance -= money

    def __str__(self):
        return f"{self.owner}: {self.balance}"

owner = input("Your name: ")
balance = float(input("Balance: "))
a = Account(owner, balance)
a.deposit()
print(a)
a.withdraw()
print(a)
a.withdraw()
print(a)
a.deposit()
print(a)
print('-----')

#6
def isprime(x):
    if int(x) == 1:
        return False
    for i in range(2, int(x)):
        if int(x) % i == 0:
            return False
    return True

l = input("List: ").split()
prime_numbers = list(filter(lambda x: isprime(x), l))
print("Prime numbers:", *prime_numbers)