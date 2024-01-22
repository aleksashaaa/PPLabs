thislist = ["apple", "banana", "cherry"]
print(thislist[1])

print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)