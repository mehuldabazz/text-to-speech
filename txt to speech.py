import os
from tkinter import *
from gtts import gTTS
from playsound import playsound
import time

# Create a directory for temporary audio files if it doesn't exist
temp_audio_dir = "temp_audio"
if not os.path.exists(temp_audio_dir):
    os.makedirs(temp_audio_dir)

# Function to convert text to speech and play the audio
def text_to_speech():
    mytext = text_entry.get("1.0", END).strip()  # Get text from text entry widget
    if mytext:
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        
        # Generate a unique filename using the current timestamp
        temp_audio_path = os.path.join(temp_audio_dir, f"welcome_{int(time.time())}.mp3")
        try:
            myobj.save(temp_audio_path)
            playsound(temp_audio_path)
        except PermissionError as e:
            status_label.config(text=f"Permission error: {e}")
        except Exception as e:
            status_label.config(text=f"Error: {e}")
    else:
        status_label.config(text="Please enter some text.")

# Creating the main window
root = Tk()
root.title("Text to Speech Converter")

# Creating and placing the text entry widget
text_entry = Text(root, wrap=WORD, width=50, height=10, font=("Arial", 12))
text_entry.pack(pady=20)

# Creating and placing the convert button
convert_button = Button(root, text="Convert to Speech", command=text_to_speech, font=("Arial", 12))
convert_button.pack(pady=10)

# Creating and placing the status label
status_label = Label(root, text="", font=("Arial", 12))
status_label.pack(pady=10)

# Running the main event loop
root.mainloop()
