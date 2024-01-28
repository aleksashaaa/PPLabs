from itertools import permutations
import math
from random import randint

#1
def gramms_to_ounces(grams):
    return 28.3495231 * grams

print(gramms_to_ounces(100))
print('-----')

#2
def F_to_C(Far):
    C = (Far - 32) * 5 / 9
    return C

print(F_to_C(100))
print('-----')

#3
def solve(numheads, numlegs):
    xc = numheads * 2
    nr = (numlegs - xc) / 2
    nc = numheads - nr
    return ("Rabbits: " + str(nr) + "\n" + "Chickens: " + str(nc))

print(solve(35, 94))
print('-----')

#4
def isprime(x):
    if int(x) == 1:
        return False
    for i in range(2, int(x)):
        if int(x) % i == 0:
            return False
    return True

def filter_prime(list):
    res = []
    for x in list:
        if isprime(x):
            res.append(x)
    return res

list = input("print the numbers: ")
print(*filter_prime(list.split()))
print('-----')

#5
def print_permutations():
    inp = input("String: ")
    perm_list = permutations(inp)
    print("Permutations:")
    for x in perm_list:
        print("".join(x))

print_permutations()
print('-----')

#6
def rev(s):
    return s[::-1]

string = input("Print the string: ")
print(*rev(string.split()))
print('-----')

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if (nums[i] == 3 and nums[i + 1] == 3):
            return True
    return False

print(has_33([1, 3, 3])) #? True
print(has_33([1, 3, 1, 3])) #? False
print(has_33([3, 1, 3])) #? False
print('-----')

#8
def spy_game(nums):
    if 0 in nums:
        zero1 = nums.index(0)
        del nums[zero1]
        if 0 in nums:
            zero2 = nums.index(0) + 1
            if 7 in nums:
                seven = nums.index(7) + 1
                if zero1 < zero2 and zero2 < seven:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


print(spy_game([1,2,4,0,0,7,5])) #--> True
print(spy_game([1,0,2,4,0,5,7])) #--> True
print(spy_game([1,7,2,0,4,5,0])) #---> False
print('-----')

#9
def volume(r):
    return 4/3*math.pi*(r**3)

r = float(input("Radius = "))
print("Volume =", volume(r))
print('-----')

#10
def unique_l(l):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return res

s = input("List: ")
print("Unique list:", *unique_l(s.split()))
print('-----')

#11
def palindrome(s):
    if s[::-1] == s:
        return True
    return False

s = input("Write a word: ")
print(palindrome(s))
print('-----')

#12
def histogram(l):
    for i in l:
        print("*" * int(i))

l = input("List:")
histogram(l.split())
print('-----')

#13
def guess_game(guess, answ, n, name):
    if guess == answ:
        out = "Good job, {}! You guessed my number in {} guesses!"
        print(out.format(name, n))
        return guess
    elif answ > guess:
        print("Your guess is too low.")
        n += 1
        guess = int(input("Take a guess.\n"))
        guess_game(guess, answ, n, name)
    else:
        print("Your guess is too high.")
        n += 1
        guess = int(input("Take a guess.\n"))
        guess_game(guess, answ, n, name)

name = input("Hello! What is your name?\n")
s = "Well, {}, I am thinking of a number between 1 and 20."
print(s.format(name))
guess = int(input("Take a guess.\n"))
answ = randint(1, 21)
n = 1
guess_game(guess, answ, n, name)