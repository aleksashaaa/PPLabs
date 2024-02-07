#1  A variable created inside a function is available inside that function:
def myfunc():
    x = 100
    print(x)

myfunc()

#2
def myfunc():
    x = 200
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

#3
x = 300

def myfunc():
    print(x)

myfunc()
print(x)

#4
x = 300

def myfunc():
    x = 200
    print(x)

myfunc() #200
print(x) #300

#5
def myfunc():
    global x
    x = 500

myfunc()
print(x)