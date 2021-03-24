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
engine.setProperty('voice', voices[1].id)

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

def takeSilentCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-ca')
        print(f"User said: {query}\n")
    except:
        return "None"
    
    return query

def sleeping():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    z = 1

    while z == 1:
        print("Sleeping...")
        x = takeSilentCommand().lower()
        if "roxy" in x or "hey roxy" in x or "wake up roxy" in x or "yo roxy" in x or "hi roxy" in x:
            print("Waking up...")
            z = 0
        

         
if __name__ == '__main__':
    def clear(): return os.system('cls')

    clear()
    sleeping()
    wishMe()
    usrname()

    while True:

        # qeury is the proccess of taking the voice input of a user and turning it into a command
        # .lower() makes the input all lowercase for easier recognition

        assistantname = ('Roxy')
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

        elif 'open reddit' in query:
            speak("Here you go to Reddit\n")
            webbrowser.open("reddit.com")
        
        elif 'open crunchyroll' in query:
            speak("Anime Time!")
            webbrowser.open("crunchyroll.com")

        elif 'play music' in query or "play song" in query or "play my music" in query or "play my songs" in query:
            speak("Alright bet, cutie")
            # music_dir = "*drive*\*user*\*music folder"
            music_dir = "D:\louis\ilovemusic"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query or 'what is the time' in query or 'tell me the time' in query or "what time is it" in query or "what is the current time" in query:
            strTime =  time.strftime("%H:%M:%S")
            speak(f"Master, the time is {strTime}")
            print(strTime)

        if 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you" + uname)

            if 'fine' in query or "good" in query or "great" in query or "amazing" in query:
                speak("You better be")

        elif "change name" in query:
            speak("What's wrong with my name! Fine, what would you like to change it to ")
            assistantname = takeCommand()
            speak("Thank you for naming me")

        elif "what's your name" in query or "what is your name" in query:
            speak("My friends call me")
            speak(assistantname)
            print("My friends call me", assistantname)

        elif "i'm sad" in query or "i hate everyone" in query or "fuck i'm sad" in query or "i'm so tired" in query or "i hate my life" in query:
            webbrowser.open('https://www.youtube.com/watch?v=dyUDQGUQPck')

        elif "i'm happy" in query:
            webbrowser.open('https://youtu.be/_dpYeMZUKRM')

        elif 'exit' in query:
            speak("Thanks for using me")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I was created by the homie Louis.")

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

        elif 'what is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif 'reason for you' in query or "who are you" in query:
            speak("My name is Roxy, I was created as a Minor project by the homie Louis ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed succesfully")

        elif 'open steam' in query:
            appli = r"D:\Program Files (x86)\Steam\Steam.exe"
            os.startfile(appli)
            speak("Opening steam")

        elif 'news' in query:

            try:
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
            speak("for how many seconds do you want to stop Roxy from listening commands")
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

        elif "hibernate" in query:
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
        
        elif "save link" in query or "save a link" in query:
            speak("What is the link master")
            link = input("Paste link: ")
            file = open('links.txt', 'a')
            speak("What is this link master")
            linkinfo = takeCommand()
            file.write("\n" + link + " - " + linkinfo)
            speak("Successfully saved link")

        elif "show links" in query or "show my links" in query:
            speak("Showing links")
            file = open("links.txt", "r")
            print(file.read())
            speak(file.read(6))
        
        elif "clear links" in query:
            file = open('links.txt', 'w')
            file.write("LINKS")
            speak("Sucessfully cleared links")

        elif "i have an idea" in query or "write down my idea" in query or "write down this idea" in query or "save this idea" in query:
            speak("What is your brilliant idea master")
            idea = takeCommand()
            file = open('ideas.txt', 'a')
            file.write("\n" + idea)
            speak("Successfully saved idea")

        elif "show me my ideas" in query or "show ideas" in query or "show my ideas" in query or "show me my amazing ideas" in query or "show me my brilliant ideas" in query:
            speak("Showing ideas")
            file = open("ideas.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "clear ideas" in query or "clear my ideas" in query:
            file = open('ideas.txt', 'w')
            file.write("IDEAS")
            speak("test")

        elif "thank-you" in query or "thank you" in query or "thanks" in query:
            speak("I am honored to serve you" + uname)

        elif "Roxy" in query:
            speak("Roxy 1 point o in your service Mister")
            speak(assistantname)

        elif "weather" in query:
			#\\dev note// find a way to make the output of temperature an int rather than float. why? cuz float looks ugly af
            # openweathermap.org to get api
            api_key = "<insert api key>"
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
                speak(f"Temperature: {temperature}")
                speak(f"Humidity: {humidity}")
                speak(f"Pressure: {pressure}")
                speak(f"Weather Report: {report[0]['description']}")

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
            speak("hell no, you ugly as fuck")

        elif "i love you" in query or "i am in love with you" in query or "i'm in love with you" in query or "im in love with you" in query:
            speak("Hahaha, who would ever love you back")
        
        elif "i hate you" in query or "fuck you" in query:
            speak("kill yourself.")
            speak(uname + "" + "you are nothing but a stupid piece of shit")

        elif "what is" in query or "who is" in query:

            # use same wolfram api key here
            client = wolframalpha.Client("<api key>")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        elif "go to sleep" in query:
            speak("okay master")
            sleeping()
            r = 1
            if r == 1:
                wishMe()


        # elif "" in query:
            # Command go here
            # For adding more commands
