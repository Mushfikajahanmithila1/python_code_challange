a = input("Enter a number between 5 to 9: ")

if("quit" in a ):
    print("Programe stopped.")
else:
    a = int(a)
    if (a < 5 or a > 9):
        raise ValueError("Please enter a number between 5 to 9")
