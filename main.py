import SpeechRecognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


#dectects Microphone input and gives the virtual assistant a name.
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


#this starts up the virtual assistant
def run_dave():
    command = take_command()
    print(command)
    if 'play' in command:  #first command in the virtual assistant
        song = command.replace('play', '')  #names the command play
        talk('playing' + song)  #makes the virtual assistant play the song
        pywhatkit.playonyt(song)  #grabs the song from youtube
    elif 'time' in command:  #time command
        time = datetime.datetime.now().strftime(
            '%I:%M %p'
        )  #tkaes the date and time from the pc name so it can print local time
        print(time)  #sends it into a command prompt
        talk('the current time is' + time)  #talks out the time
    elif 'goodbye' in command:
        talk('thank you for listening, are there anyquestions')
    elif 'introduce yourself' in command:
        talk(
            'Hi, im dave, a virtual assistant, i was programmed by ethan, and i will never be a real person'
        )
    elif 'who is' in command:
        search = command.replace('who is', '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
    elif 'where is' in command:
        search = command.replace('where is', '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
    elif 'Tell me a joke' in command:
        talk(pyjokes.get_joke())
        print(talk)
    elif 'what month is it' in command:
      time = datetime.datetime.now().strftime(
        '%M'
      )
      print(time)
      talk('We are currently in the month of' + time)
    elif 'What year is it' in command:
      time = datetime.datetime.now().strftime(
        '%Y'
      )
      print(time)
      talk('The year is ' + time)
    elif 'Easter Egg' in command:
      egg = talk('you how found the secret easter egg')
      egg
    elif 'dave' in command:#
      egg
      
    else:
        talk("Try again. speak clearly")


while True:
    run_dave
