import time

#1
s = [int(x) for x in input().split()]
print("sum:", sum(s))
print("-----")

#2
s = input()
upp = sum(1 for x in s if x.isupper())
low = sum(1 for x in s if x.islower())
print(f"Lower: {low}, Upper: {upp}")
print("-----")

#3
s = input()
print("Palindrome?", "".join(reversed(s)) == s)
print("-----")

#4
n = int(input())
t = int(input())
time.sleep(t / 1000)
result = pow(n, 0.5)
print(f"Square root of {n} after {t} miliseconds is {result}")
print("-----")

#5
tupl = tuple(("one", "two", "three", 1))
print(all(tupl)) #True
tupl = tuple(("one", "two", "three", 1, 0))
print(all(tupl)) #False