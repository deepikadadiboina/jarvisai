import speech_recognition as sr
import pyttsx3 as pt
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki
command=" "


listener = sr.Recognizer()
speaker = pt.init()
rate = speaker.getProperty('rate')
speaker.setProperty('rate',170)
va_name='cherry'
def speak(text):
    speaker.say("yes boss"+text)
    speaker.runAndWait()

def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()
speak_ex('i am your' +va_name +" ,tell me boss")
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if va_name in command:
                command=command.replace(va_name +' ','')
               # print(command)
               # speak(command)
    except:
        print("check your microprocessor once")
    return command
while True:
    user_command=take_command()
    if 'close' in user_command:
        print('see you again boss. i will be there when ever you call me.')
        speak('see you again boss. i will be there when ever you call me.')
        break
    elif 'time' in user_command:
        cur_time=dt.datetime.now().strftime("%I:%M %p")
        print(cur_time)
        speak(cur_time)
    elif 'play' in user_command:
        user_command=user_command.replace('play'," ")
        print("playing"+user_command)
        speak("playing"+user_command+", enjoy boss.")
        pk.playonyt(user_command)
        break
    elif 'search for' in user_command or 'google' in user_command:
        user_command=user_command.replace('search for','')
        user_command = user_command.replace('google', '')
        print(user_command)
        speak("searching for"+user_command)
        pk.search(user_command)
    elif 'who is' in user_command or 'about' in user_command:
        user_command=user_command.replace('who is',"")
        user_command = user_command.replace('about', "")
        info=wiki.summary(user_command,4)
        print(info)
        speak(info)
    elif 'who are you' in user_command:
        user_command=user_command.replace('who are you','')
        speak("i am your voice over sir")
    elif 'how are you' in user_command:
        user_command = user_command.replace('how are you', '')
        speak("i am fine ,thankyou. how do you do")

    else:
        speak_ex("please, say it again boss")




