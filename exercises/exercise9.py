import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

l = ["Mushfikur", "Mushfika", "Mabiya", "Kon kon", "Anushka", "Mahrine Arfi"]
for i in l:
    speaker.Speak(f"Shoutout to {i}")
    print(f"Shoutout to {i}")