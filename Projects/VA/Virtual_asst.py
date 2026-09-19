"""
#gTTs -->Google text to Speech

from gtts import gTTS
text = gTTS("Hello guy's,how are you doing?")
text.save("audio.mp3")

#playsound-->pip install playsound==1.2.2
#pyaudio-->pip install pyaudio

from gtts import gTTS
import playsound
text=gTTS("Hello guy's,how are you doing?")
#text.save("audio.mp3")
playsound.playsound("audio.mp3")

Functions-->1)Listen (SpeechRecognition)
2) Respond (gtts)
3) Assistant(conditions) --> Conversation,Greeting,datetime
Locate a place,open a browser,play a youtube video

#IMPORT THE LIBRARIES


#Import the libararies

from gtts import gTTS
import playsound
import time
import webbrowser    #it is default
import uuid          #It is default
import speech_recognition as sr
import os

#let uss create listen function

def listen():
    Function for Speech Recognition
    r = sr.Recognizer()
    #we will take micro phone as source
    with sr.Microphone() as source:
        print("Ika modeledadamma")
        audio = r.listen(source,phrase_time_limit=10)  #pharse_time_limit is adefault argument
    #we need to give our text as voice
    data = ""
    #here i will give exceptions(try,except)
    try:
        data = r.recognize_google(audio)
        print("You said: ",data)
        
    except sr.UnknowValueError as e:
        print("request Failed")

    except sr.RequestError as e:
        print("speak clearly request is failing")

    return data
    #tts=gTTS(data)
    #tts.dave("new.mp3")
    #playsound.playsound("new.mp3")

#listen()

def respond(String):
    Function to respond back
    print(String)
    tts=gTTS(String)
    tts.save("speech.mp3")

    #we using uuid --.to randomize the content in the audio file
    filename="speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# Here we will make our virtual assistant int action

def va(data):
    Our Virtual Assistant with the actions
    if "how are you" in data:
        listening=True
        respond("I am fine thanks for asking")
        
    elif "what are you plans" in data:
        listening=True
        respond("Only Study..One focus in 2026")

    elif "how are things going" in data:
        listening=True
        respond("Anthaa Okay inka nene set avvali")

    elif "Time" in data:
        listening=True
        respond(time.ctime())

    elif "open google" in data:
        listening=True
        respond("opening google")
        webbrowser.open("https://www.google.com/")
        
    elif "open whatsapp" in data:
        listening=True
        respond("opening whatsapp")
        webbrowser.open("https://web.whatsapp.com/")
        
    elif "open github" in data:
        listening=True
        respond("opening github")
        webbrowser.open("https://github.com/")

    elif "open youtube" in data:
        listening=True
        respond("playing song")
        webbrowser.open("https://www.youtube.com/")

    elif"stop talking" in data:
        listening=False
        respond("Okay cool...kopadaku bye")

    try:
        return listening

    except UnboundLocalError as e:
        print(" Make Sure speak louder and Faster")

respond("Hey Megha ...Good to hear from you.How are you?")


listening=True
while listening:
    data = listen()
    listening=va(data)

#Links:
    
#https://github.com/       ----> GitHub
#https://web.whatsapp.com/ ----> Whatsapp
#https://www.google.com/   ----> Google
#https://www.youtube.com/  ----> Youtube
#Virtual Assistant --> QRCode,Play a Game  """


#Import the libraries
from gtts import gTTS
import playsound
import time
import webbrowser       #it is default
import uuid             #it is default
import speech_recognition as sr
import os
import random
import Module

#let us create listen function
def listen():
    """Function for Speech Recogntion"""
    r = sr.Recognizer()
    #we will take microphone as source
    with sr.Microphone() as source:
        print("Ika modaledadamma")
        audio = r.listen(source,phrase_time_limit = 10)  #pharse_time_limit is adefault argument
    #we need to give our text as voice
    data= ""
    #here we will give exceptions (try,except)
    try:
        data = r.recognize_google(audio)
        print("You said:",data)
    except sr.UnknownValueError as e:
        print("Request Failed")
    except sr.RequestError as e:
        print("Speak clearly request is failing")
    return data
#listen()
    #tts = gTTS(data)
    #tts.save("new.mp3")
    #playsound.playsound("new.mp3")
#listen()
        
def respond(String):
    """Function to respond back"""
    print(String)
    tts = gTTS(String)
    tts.save("Speech.mp3")
    #we are using uuid --> to randomize the content in the
    #audio file
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# QR Code function
def qr_code():
    """open the QR Code"""

    respond("Opening your QR code")

    os.startfile("myqr.png")

def play_game():    #Random Number Generator 
    #Guess the Number Game

    number = random.randint(1, 10)

    respond("I have selected a number between 1 and 10")

    respond("Try to guess the number")

    guess = int(input("Enter your guess: "))

    if guess == number:
        respond("Congratulations! You guessed it correctly")

    else:
        respond("Sorry, the correct number was " + str(number))

#here we will make our virtual assitant into action
def va(data):
    """Our Virtual Assistant with the actions"""
    if "how are you" in data:
        listening = True
        respond("I am fine thanks for asking")
    elif "what are your plans" in data:
        listening = True
        respond("Only Study..One focus in 2026")
    elif "how are things going" in data:
        listening= True
        respond("Anthaa okay ika nene set avali")
    elif "time" in data:
        listening = True
        respond(time.ctime())
    elif "locate" in data:
        listening = True
        webbrowser.open(
            "https://www.google.com/maps/search/"
            + data.replace("locate",""))
        respond("Located")
    elif "open Google" in data:
        listening = True
        webbrowser.open("https://www.google.com")
        respond("Opened")
    elif "qr code" in data:
        listening = True
        qr_code()
    elif "play game" in data:
        listening=True
        play_game()
    elif "stop talking" in data:
        listening = False
        respond("okay cool..kopadakuu bye")
    try:
        return listening
    except UnboundLocalError as e:
        print("Make sure to speak louder and faster")

respond("Hey Megha..Good to hear from you.How are you?")    
listening = True
while listening:
    data = listen()
    listening = va(data)

#Finish your tasks --> Choice of games -->Github links """




    
        
         
        
        
        
    
        
        
        
        
    



