import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Open the microphone and capture audio
with sr.Microphone() as source:
    print("Please start speaking...")
    audio = recognizer.listen(source)

# Recognize speech using Google Web Speech API
try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")
