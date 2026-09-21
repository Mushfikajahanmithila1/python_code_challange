a = 5
b = 5
print(a is b) # compare the exact location of object in memory
print(a == b) # compare the value


c = [3, 4, 5]
d = [3, 4, 5]
print(c is d) # flase
print(c == d) # true

e = (3, 5, 3)
f = (3, 5, 3)
print(e is f)
print(e == f)