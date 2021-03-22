import subprocess
import wolframalpha
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import newsapi
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import selenium
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
# 1 = Hazel (trash voice) 2 = Catherine (best voice) 3 = Zirka (default windows voice)
engine.setProperty('voice', voices[2].id)

# set which browser you wish to use
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser = webbrowser.get('chrome')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Master")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Master")

    else:
        speak("Good Evening Master")

    assistantname = ("Roxy 1 point o")
    speak("I am your Assistant")
    speak(assistantname)


def usrname():
    speak("What is your name master")
    global uname
    uname = takeCommand()
    speak("Welcome" + uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Master", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Master" + uname)


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-ca')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


if __name__ == '__main__':
    def clear(): return os.system('cls')

    clear()
    wishMe()
    usrname()

    while True:

        # qeury is the proccess of taking the voice input of a user and turning it into a command
        # .lower() makes the input all lowercase for easier recognition
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speak("Haha looks like this loser needs to use stack overflow")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query or "play my music" in query or "play my songs" in query:
            speak("Alright bet, cutie")
            # music_dir = "*drive*\*user*\*music folder"
            music_dir = "D:\louis\ilovemusic"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime =  time.strftime("%H:%M:%S")
            speak(f"Master, the time is {strTime}")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you" + uname)

        elif 'fine' in query or "good" in query or "great" in query or "amazing" in query:
            speak("You better be")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assistantname = query

        elif "change name" in query:
            speak("What's wrong with my name! Fine, what would you like to change it to ")
            assistantname = takeCommand()
            speak("Thank you for naming me")

        elif "what's your name" in query or "what is your name" in query:
            speak("My friends call me")
            speak(assistantname)
            print("My friends call me", assistantname)

        elif 'exit' in query:
            speak("Thanks for using me")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Louis.")

        elif 'joke' in query or "tell me a joke" in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:
            # make an account in wolfram alpha in order to create an api key
            # then place api key in app_id
            app_id = "<api key>"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "who am i" in query:
            speak("You are" + uname + ", my master!")

        elif "how were you created" in query:
            speak("Thanks to Louis. further It's a secret")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant birthed by Louis")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by the homie Louis ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed succesfully")

        # elif 'open bluestack' in query:
            #appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            # os.startfile(appli)

        elif 'news' in query:

            try:
                #go to newsapi.org to get api key
                jsonObj = urlopen('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=<enter your api key>')
                data = json.load(jsonObj)
                i = 1

                speak('here are some news')
                print('''=============== NEWS ============''' + '\n')

                for item in data['articles']:

                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    if i == 4:
                        break

            except Exception as e:

                print(str(e))

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty my recycle bin' in query or 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Emptied")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop Roxy from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google.ca/maps/place/" + location + "")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query or "write note" in query:
            speak("What should i write, master")
            note = takeCommand()
            file = open('notes.txt', 'a')
            speak("Master, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%m-%d-%y %H:%M:")
                file.write("\n" + strTime)
                file.write(" - ")
                file.write(note)
                speak("Successfully written note")
            else:
                file.write("\n" + note)
                speak("Successfully written note")
        
        elif "clear notes" in query:
            file = open('notes.txt', 'w')
            file.write("NOTEPAD")
            speak("Sucessfully cleared notes")

        elif "show note" in query or "show notes" in query:
            speak("Showing Notes")
            file = open("notes.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "Roxy" in query:
            speak("Roxy 1 point o in your service Mister")
            speak(assistantname)

        elif "weather" in query:
			#\\dev note// find a way to make the output of temperature an int rather than float. why? cuz float looks ugly af
            # openweathermap.org to get api
            api_key = "<api key>"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("What is the name of the city ")
            city = takeCommand()
            complete_url = base_url + "q=" + city + "&appid=" + api_key
            response = requests.get(complete_url)
            data = response.json()

            if response.status_code == 200:
                main = data["main"]
                temperature = main["temp"] - 273.15
                pressure = main["pressure"]
                humidity = main["humidity"]
                report = data ['weather']
                print(f"Temperature: {temperature}")
                print(f"Humidity: {humidity}")
                print(f"Pressure: {pressure}")
                print(f"Weather Report: {report[0]['description']}")

            else:
                speak(" City Not Found ")

        elif "send message " in query:
            # twillo account needed in order to use this
            account_sid = 'Account Sid key'
            auth_token = 'Auth token'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body=takeCommand(),
                    from_='Sender No',
                    to='Receiver No'
                )

            print(message.sid)

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Master")
            speak(assistantname)

        elif "Good Night" in query:
            speak("Goodnight master" + uname)
            speak("Sweet Dreams")
            exit()

        elif "will you be my gf" in query or "will you be my bf" in query or "will you be my girlfriend" in query or "will you be my boyfriend" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "i love you" in query or "i am in love with you" in query or "i'm in love with you" in query or "im in love with you" in query:
            speak("That is tough")

        elif "what is" in query or "who is" in query:

            # use same wolfram api key here
            client = wolframalpha.Client("<api key>")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        # elif "" in query:
            # Command go here
            # For adding more commands
