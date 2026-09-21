a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
w = input("Which operation you want to create with numbers: ")

if("+" in w):
    print(a+b)
elif("-" in w):
    print(a-b)
elif("*" in w):
    print(a*b)
elif("/" in w):
    print(a/b)
elif("//" in w):
    print(a//b)
elif("**" in w):
    print(a**b)
elif("%" in w):
    print(a%b)
else:
    print("Invalid number.")