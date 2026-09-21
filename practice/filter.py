def is_greater(b):
    return 3 < b

l = [1, 3, 4, 5 ,3, 8, 8, 9, 2]
f = list(filter(is_greater, l))
print(f)