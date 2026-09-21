import time

ranth = int(time.strftime("%H"))
rantm = int(time.strftime("%M"))
rants = int(time.strftime("%S"))

if(ranth < 13):
    print("good morning")
elif(ranth < 18):
    print("good noon")
elif(ranth < 19):
    print("good evening")
else:
    print('good night')