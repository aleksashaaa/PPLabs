#1
n = int(input())

def square(n):
    i = 1
    while i**2 <= n:
        yield i**2
        i += 1

for i in square(n):
    print(i)
print("-----")

#2
n = int(input())

def even(n):
    i = 0
    while(i <= n):
        if i % 2 == 0:
            yield str(i)
        i += 1

l = list(even(n))
print(", ".join(l))
print("-----")

#3
n = int(input())

def even(n):
    i = 0
    while(i <= n):
        if i % 3 == 0 and i % 4 == 0:
            yield str(i)
        i += 1

l = list(even(n))
print(", ".join(l))
print("-----")

#4
a = int(input())
b = int(input())

def squares(a, b):
    if (a < b):
        i = a
        while i <= b:
            yield i**2
            i += 1
    else:
        i = a
        while i >= b:
            yield i**2
            i -= 1

for i in squares(a, b):
    print(i)
print("-----")

#5
n = int(input())

def gen(n):
    i = n
    while i > 0:
        yield i
        i -= 1

for i in gen(n):
    print(i)