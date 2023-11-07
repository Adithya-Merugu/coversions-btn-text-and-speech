from gtts import gTTS
import os

# Specify the path to the text file
text_file_path = "input.txt"

# Read the text from the file
with open(text_file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Initialize the gTTS object and specify the language (you can change it to your preferred language)
tts = gTTS(text, lang="en")

# Save the speech as an audio file (e.g., output.mp3)
tts.save("output.mp3")

# Play the audio using your system's default media player (e.g., VLC, Windows Media Player)
os.system("start output.mp3")  # On Windows
# Use a different command for your OS to play the audio if you're not on Windows
