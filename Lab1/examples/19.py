#mistake
'''
txt = "We are the so-called "Vikings" from the north."
'''

txt = "We are the so-called \"Vikings\" from the north."

# some methods
x = "asdkTlcORcm"
print(x.capitalize()) 
print(x.casefold())
print(x.encode())
print(x.swapcase())

txt = "banana"
x = txt.center(20, "O")
print(x)

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)