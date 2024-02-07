import math

#1
n = float(input())
print(f"{n} in radians = {math.radians(n)}")
print("-----")

#2
height = int(input())
a = int(input())
b = int(input())
print((a + b)/ 2 * height)
print("-----")

#3
num = int(input())
l = float(input())
S = (num * l ** 2) / (4 * math.tan(math.pi / num))
print(S)
print("-----")

#4
h = float(input())
a = float(input())
print(a * h)
