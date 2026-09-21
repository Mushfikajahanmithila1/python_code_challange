import random
import string

# take string
st = input("Enter your massage: ")
coding = input("Enter 1 for coding or enter 0 for decoding: ")
words = st.split(" ")
coding = True if coding == "1" else False

# for coding
if coding:
    newwords = []

    for word in words:
        if(len(word) >=3 ):
            ran1 = "".join(random.choices(string.ascii_lowercase, k=3))
            ran2 = "".join(random.choices(string.ascii_lowercase, k=3))
            newword = ran1 + word[1:] + word[0] + ran2
            newwords.append(newword)
        else:
            newwords.append(word[::-1])
            print("".join(newwords))
else:
    newwords = []
    for word in words:
        if(len(word) >= 3):
            newword = word[3:-3]
            newword = newword[-1] + newword[:-1]
            newwords.append(newword)
        else:
            newwords.append(word[::-1])
            print("".join(newwords))
