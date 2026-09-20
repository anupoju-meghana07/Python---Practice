# Import the libraries
from gtts import gTTS
import playsound
import time
import webbrowser
import uuid
import speech_recognition as sr
import os
import random

# LISTEN FUNCTION

def listen():
    """Function for Speech Recognition"""

    r = sr.Recognizer()

    # Take microphone as source
    with sr.Microphone() as source:
        print("Ika modaledadamma")
        audio = r.listen(source, phrase_time_limit=10)

    data = ""

    # Speech recognition
    try:
        data = r.recognize_google(audio)
        print("You said:", data)

    except sr.UnknownValueError as e:
        print("Request Failed")

    except sr.RequestError as e:
        print("Speak clearly request is failing")

    return data

# RESPOND FUNCTION

def respond(String):
    """Function to respond back"""

    print(String)

    tts = gTTS(String)

    # Create a random audio file
    filename = "Speech%s.mp3" % str(uuid.uuid4())

    tts.save(filename)

    playsound.playsound(filename)

    # Delete the audio file
    os.remove(filename)

# QR CODE FUNCTION

def qr_code():
    """Open the QR Code"""

    respond("Opening your QR code")

    #  QR image is named throwback.png
    if os.path.exists("throwback.png"):
        os.startfile("throwback.png")
    else:
        print("QR Code file not found")
        respond("QR code file not found")

# GUESS THE NUMBER GAME

def play_game():
    """Guess the Number Game"""

    number = random.randint(1, 10)

    respond("I have selected a number between 1 and 10")

    respond("Try to guess the number")

    guess = int(input("Enter your guess: "))

    if guess == number:
        respond("Congratulations! You guessed it correctly")

    else:
        respond("Sorry, the correct number was " + str(number))


# VIRTUAL ASSISTANT

def va(data):
    """Our Virtual Assistant with the actions"""

    if "how are you" in data:
        listening = True
        respond("I am fine thanks for asking")

    elif "what are your plans" in data:
        listening = True
        respond("Only Study..One focus in 2026")

    elif "how are things going" in data:
        listening = True
        respond("Anthaa okay ika nene set avali")

    elif "time" in data:
        listening = True
        respond(time.ctime())

    elif "locate" in data:
        listening = True

        webbrowser.open(
            "https://www.google.com/maps/search/"
            + data.replace("locate", "")
        )

        respond("Located")

    elif "open google" in data:
        listening = True

        webbrowser.open("https://www.google.com")

        respond("Opened")

    # QR CODE
    elif "qr code" in data:
        listening = True
        qr_code()

    # PLAY GAME
    elif "play game" in data:
        listening = True
        play_game()

    # STOP
    elif "stop talking" in data:
        listening = False
        respond("okay cool..kopadakuu bye")

    else:
        listening = True
        print("Command not recognized")

    return listening

# START VIRTUAL ASSISTANT
respond("Hey Megha..Good to hear from you. How are you?")
listening = True
while listening:
    data = listen()
    # Convert speech to lowercase
    data = data.lower()
    listening = va(data)
