import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import re 
from twilio.rest import TwilioRestClient

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'manager' in command:
                command = command.replace('manager', '')
                print(command)
    except:
        pass
    return command
def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    TWILIO_PHONE_NUMBER = ""

# list of one or more phone numbers to dial, in "+19732644210" format
    DIAL_NUMBERS = ["+91100",]

# URL location of TwiML instructions for how to handle the phone call
    TWIML_INSTRUCTIONS_URL = \
            "http://static.fullstackpython.com/phone-calls-python.xml"

# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
    client = TwilioRestClient("ACxxxxxxxxxx", "yyyyyyyyyy")
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")    


def run_manager():
    command = take_command()
    a={}
    b={}
    
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'calculate' in command:
        price=int(command.replace('calculate', ''))
        a=price-price*(10/100)
        talk(r"selling price is {a}")  
    elif 'save' in command:
        while True:
            Material=command.replace('save','')
            entity=re.search(r'[a-zA-Z_]* ', stock)
            value=re.search(r'[0-9]',stock)
            a.add('stock',value)
            if 'ok' in command:
                break
    elif 'stock' in command:
        talk('current stock is' + entity + value)
    elif 'change' in command:
        # space for open cv to recognise currency
        remaining=currency-
        pass
    elif 'sure sure sure' in command:
        dial_numbers(DIAL_NUMBERS)
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'search about' in command:
        person = command.replace('search about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('definitely when would you like to go')
    elif 'are you single' in command:
        talk('I Love You')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_manager()
