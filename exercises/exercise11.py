import time
from win32com.client import constants
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
while True:
    speaker.Speak("Time to drink water! Please, Drink your water, drink your water.")
    # print("Time to drink water!")

    print("\a")

    time.sleep(60 * 60)
