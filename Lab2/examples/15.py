x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) #how to change tuple

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) #how to add
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) #add tuple to tuple

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y) # remove 
print(thistuple) 

thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists