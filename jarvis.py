import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import cv2
import numpy as np

# Voice engine setup
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech recognizer
r = sr.Recognizer()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("You said:", command)
            return command.lower()

        except:
            return ""

# Green Jarvis UI
def jarvis_ui(text="JARVIS ONLINE"):
    img = np.zeros((500, 800, 3), np.uint8)

    cv2.putText(
        img,
        text,
        (50, 250),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 255, 0),
        3
    )

    cv2.imshow("JARVIS", img)
    cv2.waitKey(1)

# Start Jarvis
speak("Jarvis Activated")
jarvis_ui("JARVIS ACTIVATED")

while True:

    command = take_command()

    if "time" in command:

        time = datetime.datetime.now().strftime("%I:%M %p")

        speak("Current time is " + time)
        jarvis_ui("TIME: " + time)

    elif "open youtube" in command:

        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
        jarvis_ui("OPENING YOUTUBE")

    elif "open google" in command:

        speak("Opening Google")
        webbrowser.open("https://google.com")
        jarvis_ui("OPENING GOOGLE")

    elif "play music" in command:

        speak("Playing music")
        webbrowser.open("https://open.spotify.com")
        jarvis_ui("PLAYING MUSIC")

    elif "who are you" in command:

        speak("I am Jarvis, your AI assistant")
        jarvis_ui("I AM JARVIS")

    elif "bye" in command or "exit" in command:

        speak("Goodbye boss")
        jarvis_ui("SYSTEM SHUTDOWN")
        break

    elif command != "":

        speak("Sorry, I didn't understand")
        jarvis_ui("UNKNOWN COMMAND")

cv2.destroyAllWindows()