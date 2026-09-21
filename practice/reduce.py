from functools import reduce
l = [1, 3, 4, 5 ,3, 8, 8, 9, 2]
redu = reduce(lambda x,y: x + y, l)

print(redu)