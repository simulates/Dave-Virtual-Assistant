import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime 
import wikipedia 

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'dave' in command:
                command = command.replace('dave', '')
                print("given command:", command)
                
    except:
        pass
    return command

def run_dave():
    command = take_command()
    print (command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('the current time is' + time)
    elif 'goodbye' in command:
        talk('thank you for listening, are there anyquestions')
    elif 'introduce yourself' in command:
        talk('Hi, im dave, a virtual assistant, i was programmed by ethan, and i will never be a real person')    
    elif 'who is' in command:
        search = command.replace('who is', '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
    else:
        talk("Try again. speak clearly")




while True:
    run_dave