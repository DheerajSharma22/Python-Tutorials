import win32com.client

userToGiveShoutOut = ["Dheeraj", "Neeraj", "Radhika", "Rahul", "Summer", "Rohan"]

speaker = win32com.client.Dispatch("SAPI.SpVoice")

for user in userToGiveShoutOut:
    speaker.Speak(f"Shoutout to {user}")
    