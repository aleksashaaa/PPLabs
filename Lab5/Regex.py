import re

f = open("row.txt", "r")

lines = f.readlines()
s = ""
for line in lines:
    s += line

s2 = input()

#1
print("Num 1 -", re.findall(r'ab*', s))
print("Num 1 -", re.findall(r'ab*', s2))

#2
print("Num 2 -", re.findall(r'abbb?', s))
print("Num 2 -", re.findall(r'abbb?', s2))

#3
print("Num 3 -", re.findall(r'\b[a-z]+_[a-z]+\b', s))
print("Num 3 -", re.findall(r'\b[a-z]+_[a-z]+\b', s2))

#4
print("Num 4 -", re.findall(r'[A-Z][a-z]+', s))
print("Num 4 -", re.findall(r'[A-Z][a-z]+', s2))

#5
print("Num 5 -", re.findall(r'a.*b', s))
print("Num 5 -", re.findall(r'a.*b', s2))

#6
#print("Num 6 -", re.sub(r'[ ,.]', "|", s))
print("Num 6 -", re.sub(r'[ ,.]', "|", s2))

#7 
#print("Num 7 -", re.sub(r'_([a-zA-z])', lambda m: m.group(1).upper(), s))
print("Num 7 -", re.sub(r'_([a-zA-z])', lambda m: m.group(1).upper(), s2))

#8
#print("Num 8 -", re.split(r"[A-Z]", s))
print("Num 8 -", re.split(r"[A-Z]", s2))

#9 
#print("Num 9 -", re.sub(r"([A-Z])", " \\1", s))
print("Num 9 -", re.sub(r"([A-Z])", " \\1", s2))

#10 ---
#print("Num 10 -", re.sub(r"([a-z])([A-Z])", "\\1_\\2", s).lower())
print("Num 10 -", re.sub(r"([a-z])([A-Z])", "\\1_\\2", s2).lower())
f.close()