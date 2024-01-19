x = "Hello World"
print(len(x)) #11

print(x[0]) #H

print(x[2:5]) #llo

txt = " Hello World "
print(txt.strip()) #"Hello World"

print(x.upper()) #HELLO WORLD

print(x.lower()) #hello world

print(x.replace("H", "J")) #Jello World

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))