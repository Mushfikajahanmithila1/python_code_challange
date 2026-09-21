def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning, sir.")
        result = fx(*args, **kwargs)
        print("Thanks for using this function")
        return result
    
    return mfx

@greet
def hello():
    print("hello sir")

@greet
def mul(a, b):
    return a*b 

hello()
print(mul(2,3))

# gpt
# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good morning, sir.")
#         result = fx(*args, **kwargs)
#         print("Thanks for using this function")
#         return result

#     return mfx


# @greet
# def mul(a, b):
#     return a * b


# print(mul(2, 3))