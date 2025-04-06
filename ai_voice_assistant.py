import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

r = sr.Recognizer()
phone_numbers = {'vinay':'8186986984','mummy':'924567954','daddy':'8008224508'}
bank_account_numbers = {'vinay':'123456789','karthik':'789456123'}
def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('Listening... Ask now...')
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin)
            my_text = my_text.lower()
            print(my_text)
            
            #ask to play song
            if 'play' in my_text:
                my_text = my_text.replace('play','')
                speak('playing' + my_text)
                pywhatkit.playonyt(my_text)
            #ask date 
            elif 'date' in my_text:
                today = datetime.date.today()
                speak(today)
            #ask time
            elif 'time' in my_text:
                timenow = datetime.datetime.now().strftime('%H:%M')
                speak(timenow)
            #ask details about person
            elif "tell about" in my_text:
                person = my_text.replace('tell about','')
                info = wikipedia.summary(person,1)
                speak(info)
            #ask phone numbers
            elif 'phone number' in my_text:
                names = list(phone_numbers)
                print(names)
                for name in names:
                    if name in my_text:
                        print(name + 'phone number is' + phone_numbers[name])
                        speak(name + 'phone number is' + phone_numbers[name])
            #ask bank account numbers
            elif 'account number' in my_text:
                banks = list(bank_account_numbers)
                for bank in banks:
                    if bank in my_text:
                        print(bank + 'bank account number is ' + bank_account_numbers[bank])
                        speak(bank + 'bank account number is ' + bank_account_numbers[bank])
            else:
                speak('please provide correct question')  
    except:
        print('Error in capturing microphone...')

while True:
    commands()
