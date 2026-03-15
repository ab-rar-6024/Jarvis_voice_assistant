import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import cv2
import numpy as np
import os
import pyautogui
import psutil
import wikipedia

# ---------------- Voice Engine ----------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------- Speech Recognition ----------------
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

# ---------------- Jarvis UI ----------------
def jarvis_ui(text="JARVIS ONLINE"):

    img = np.zeros((500,800,3), np.uint8)

    cv2.putText(
        img,
        text,
        (60,250),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.1,
        (0,255,0),
        3
    )

    cv2.imshow("JARVIS", img)
    cv2.waitKey(1)

# ---------------- Start Jarvis ----------------
speak("Jarvis Activated")
jarvis_ui("JARVIS ACTIVATED")

while True:

    command = take_command()

    # TIME
    if "time" in command:

        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + time)
        jarvis_ui("TIME: " + time)

    # DATE
    elif "date" in command:

        date = datetime.datetime.now().strftime("%B %d %Y")
        speak("Today is " + date)
        jarvis_ui("DATE: " + date)

    # OPEN YOUTUBE
    elif "open youtube" in command:

        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
        jarvis_ui("OPENING YOUTUBE")

    # OPEN GOOGLE
    elif "open google" in command:

        speak("Opening Google")
        webbrowser.open("https://google.com")
        jarvis_ui("OPENING GOOGLE")

    # OPEN CHATGPT
    elif "open chat gpt" in command:

        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")
        jarvis_ui("OPENING CHATGPT")

    # PLAY MUSIC
    elif "play music" in command:

        speak("Playing music")
        webbrowser.open("https://open.spotify.com")
        jarvis_ui("PLAYING MUSIC")

    # OPEN CAMERA
    elif "open camera" in command:

        speak("Opening camera")

        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()

            cv2.imshow("Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    # TAKE SCREENSHOT
    elif "screenshot" in command:

        speak("Taking screenshot")

        img = pyautogui.screenshot()
        img.save("screenshot.png")

        jarvis_ui("SCREENSHOT SAVED")

    # CPU USAGE
    elif "cpu" in command:

        usage = psutil.cpu_percent()
        speak(f"CPU is at {usage} percent")
        jarvis_ui(f"CPU {usage}%")

    # WIKIPEDIA SEARCH
    elif "search" in command:

        speak("Searching")

        try:
            result = wikipedia.summary(command, sentences=2)
            speak(result)
            jarvis_ui("SEARCH RESULT")

        except:
            speak("I could not find anything")

    # WHO ARE YOU
    elif "who are you" in command:

        speak("I am Jarvis, your artificial intelligence assistant")
        jarvis_ui("I AM JARVIS")

    # EXIT
    elif "bye" in command or "exit" in command:

        speak("Goodbye boss")
        jarvis_ui("SYSTEM SHUTDOWN")
        break

    elif command != "":

        speak("Sorry I did not understand")
        jarvis_ui("UNKNOWN COMMAND")

cv2.destroyAllWindows()