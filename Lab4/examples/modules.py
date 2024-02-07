#1
import mymodule1 #or import mymodule1 as mx -> mx.greeting("...")

mymodule1.greeting("Jonathan")

#2
a = mymodule1.person1["age"]
print(a)

#3 built-in modules
import platform

x = platform.system()
print(x)

#4
import platform

x = dir(platform) #List all the defined names belonging to the platform module
print(x)

#5
from mymodule1 import person1

print (person1["age"])