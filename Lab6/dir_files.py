import os

#1
path = r"C:\Users\User\PPLabs\Lab4"
print("Only directories:")
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        print(name)
print("Only files:")
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        print(name)
print("All directories and files :")
for name in os.listdir(path):
    print(name)
print("-----")

#2
if os.path.exists(path):
    print(f"{path} exists")
else:
    print(f"{path} does not exist")
# Test readability
if os.access(path, os.R_OK):
    print(f"{path} is readable")
else:
    print(f"{path} is not readable")
# Test writability
if os.access(path, os.W_OK):
    print(f"{path} is writable")
else:
    print(f"{path} is not writable")
# Test executability
if os.access(path, os.X_OK):
    print(f"{path} is executable")
else:
    print(f"{path} is not executable")
print("-----")

#3
if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print(f"{path} does not exist")
print("-----")

#4
file = open("text.txt", "r")
lines = file.readlines()
print(f"There are {len(lines)} lines in file 'text.txt'")
file.close()
print("-----")

#5
list = [1, 2, 3, 4]
file = open("text.txt", "w")
file.write(" ".join([str(x) for x in list]))
file.close()
file = open("text.txt", "r")
print(file.read())
file.close()
print("-----")

#6
for i in range(65, 91):
    f = open(f"{chr(i)}.txt", "w")

#7
file = open("text.txt", "r")
x = file.read()
file.close()
file = open("A.txt", "w")
file.write(x)
file.close()
file = open("A.txt", "r")
print(file.read())
file.close()
print("-----")

#8
file = r"C:\Users\User\PPLabs\Lab6\B.txt"
if os.path.exists(file) and os.access(file, os.R_OK) and os.access(file, os.W_OK) and os.access(file, os.X_OK):
    os.remove(file)
else:
    print("The file does not exist")