import pyscreenshot as ImageGrab
import time
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
from tkinter import *
import subprocess
import requests
import random
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.did-you-knows.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
facts = []
expression = ""
# imporve needed

greet = ["hello", "hi", "aloha", "Kon'nichiwa that's hello in japanese", "nammastaa", "Bonjour that's hello in french"]
name = None

i = 0

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def facts_add(soup):
    for fact in soup.findAll('span', attrs={'class': 'dykText'}):
        facts.append(fact.text)


def next_page(soup):
    for links in soup.findAll('div', attrs={'class': 'pagePagintionLinks'}):
        if soup.findAll('a', attrs={'class': 'next'}):
            nav = links.find_all('a')[-1].get('href')
            return nav


def main():
    next_pg = ''
    Proceed = True
    try:
        while Proceed:
            url = base_url + next_pg
            response = requests.get(url, headers=headers, timeout=2)
            if response.status_code != 200:
                return False
            soup = BeautifulSoup(response.content, 'html.parser')
            facts_add(soup)
            next_pg = next_page(soup)
            if not next_pg:
                Proceed = False
    except requests.ConnectionError as e:
        print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
        print(str(e))
    except requests.Timeout as e:
        print("OOPS!! Timeout Error")
        print(str(e))
    except requests.RequestException as e:
        print("OOPS!! General Error")
        print(str(e))
    except KeyboardInterrupt:
        print("Someone closed the program")
    finally:
        print(f"Total Records  = {len(facts)}")
        print(random.choice(facts).encode('ascii', errors='ignore').decode())


def weightConverter():
    weight = int(input("Weight: "))
    unit = input("(L)bs or (K)g: ")
    if unit.upper() == "L":
        converted = weight * 0.45
        print(f"You are {converted} Kg")
    else:
        converted = weight / 0.45
        print(f"You are {converted} Lbs")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hemsharan2050@gmail.com', 'sharan12345')
    server.sendmail('hemsharan2050@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'in wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("in wikipedia", "")
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        if "in youtube" in query:
            speak('Searching youtube...')
            query = query.replace("in youtube", "")

            query = query.replace("search", "")
            query = query.replace(" ", "+")
            print(query)
            os.system(f"start https://www.youtube.com/results?search_query={query} +query ")

        if "on youtube" in query:
            speak('Searching youtube...')
            query = query.replace("on youtube", "")

            query = query.replace("search", "")
            query = query.replace(" ", "+")
            print(query)
            os.system(f"start https://www.youtube.com/results?search_query={query} +query ")
        if "in google" in query:
            speak('Searching google...')
            query = query.replace("in google", "")

            query = query.replace("search", "")
            query = query.replace(" ", "+")
            print(query)
            os.system(f"start https://www.google.com/search?query={query} +query ")
        if "on google" in query:
            speak('Searching google...')
            query = query.replace("on google", "")

            query = query.replace("search", "")
            query = query.replace(" ", "+")
            print(query)
            os.system(f"start https://www.google.com/search?query={query} +query ")
        if query in greet:
            greetnum = random.randint(1, 4)
            speak(greet[greetnum])
            print(greet[greetnum])

        if 'open yahoo' in query:
            webbrowser.open("yahoo.com")
        elif 'open notepad' in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

        elif 'open wordpad' in query:
            subprocess.Popen('C:\\Windows\\System32\\write.exe')
        elif 'open calculator' in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\vastalya-sharan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code.exe"
            os.startfile(codePath)


        elif 'open website' in query:
            speak("which website you want to open")
            web = input("which website you want to open")
            speak("opening")
            speak(web)
            webbrowser.open(web)

        elif 'timer' in query:
            speak("please enter for how much time you need timer")
            timer = int(input("please enter for how much time you need timer: "))
            speak("timer set")
            time.sleep(timer)
            speak("sir the timer has been over")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'joke' in query:
            jokeurl = "https://icanhazdadjoke.com/"
            response = requests.get(jokeurl, headers={"accept": "text/plain"})
            speak(response.text)
            print(response.text)

        elif 'story' in query:
            speak("ONCE, THERE LIVED a group then a twist and happy ending ")
            print("ONCE, THERE LIVED a group then a twist and happy ending")


        elif 'boss' in query:
            speak("you are my boss ")
            print("you are my boss")


        elif 'take screenshot' in query:
            time.sleep(2)
            im = ImageGrab.grab()
            im.save('screenshot.png')
            im.show()
            speak("screenshot Took. screenshot will be temporarly saved")



        elif 'save my name' in query:
            speak("what name do you want to save ")
            print("what name do you want to save ")
            time.sleep(2)
            name = input()
            time.sleep(2)

        elif 'jarvis' in query:
            speak("yes sir")



        elif 'my name' in query:
            if name == None:
                speak("i don't know your name")
                speak("please write your name")
                print("please write your name")
                name = input()

            speak("sir your name is "), speak(name)
            print("sir your name is", name)



        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open reddit' in query:
            webbrowser.open("reddit.com")

        elif 'open udemy' in query:
            webbrowser.open("udemy.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'how are you' in query:
            speak("I am fine sir. how may I help you")
            print("I am fine sir. how may I help you")



        elif 'what can you do' in query:
            speak(
                "i can play you music. search meanings in wikipedia. open websites.chat with you. tell a joke and much more")
            print(
                "i can play you music. search meanings in wikipedia. open websites.chat with you. tell a joke and much more")


        elif 'hate you' in query:
            print("dont say that i love you so much")
            speak("dont say that i love you so much")


        elif 'i love you ' in query:
            print("I love you too")
            speak("I love you too")


        elif 'tell your' and 'code' in query:
            print(" i am sorry sir. i cannot tell you about my code")
            speak(" i am sorry sir. i cannot tell you about my code")

        elif 'who are you' in query:
            speak("I am jarvis. your personal assistant")
            print("I am jarvis. your personal assistant")


        elif 'you born' in query:
            speak("I was born on 5 august 2019 and I am made by shearan")
            print("I was born on 5 august 2019 and I am made by sharan")


        elif 'your death' in query:
            speak("I may die in this program but I will always be present in your heart")
            print("I may die in this program but I will always be present in your heart")


        elif 'set reminder' in query:
            speak("what reminder do you want")
            remd = input("what reminder do you want: ")

            print("reminder set")
            speak("reminder set")


        elif 'my reminder' in query:

            print(remd)
            speak(remd)

        elif 'play music' in query:
            music_dir = 'D:/music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open app' in query:
            speak("enter application name please don't use any space")
            codePath = input("enter application name please don't use any space ").lower()
            os.startfile(f"D:\jarvistoopenapplications\{codePath}")
        elif 'open application' in query:
            speak("enter application name please don't use any space")
            codePath = input("enter application name please don't use any space ").lower()
            os.startfile(f"D:\jarvistoopenapplications\{codePath}")



        elif 'shutdown' in query:
            speak("are you sure you want to shut down pc ")
            shutdown = input("are you sure you want to shut down pc ").lower
            if shutdown == 'yes':
                os.system('shutdown -s')
            if shutdown == 'no':
                speak("no problem sir")


        elif "your age" in query:
            currentDate = datetime.datetime.now()

            deadline = "8/5/2019"
            deadlineDate = datetime.datetime.strptime(deadline, '%m/%d/%Y')
            print(deadlineDate)
            daysLeft = deadlineDate - currentDate
            print(daysLeft)

            years = ((daysLeft.total_seconds()) / (365.242 * 24 * 3600))
            yearsInt = int(years)

            months = (years - yearsInt) * 12
            monthsInt = int(months)

            days = (months - monthsInt) * (365.242 / 12)
            daysInt = int(days)

            hours = (days - daysInt) * 24
            hoursInt = int(hours)

            minutes = (hours - hoursInt) * 60
            minutesInt = int(minutes)

            seconds = (minutes - minutesInt) * 60
            secondsInt = int(seconds)

            print('You are {0:d} years, {1:d}  months, {2:d}  days old.'.format(yearsInt, monthsInt, daysInt, hoursInt,
                                                                                minutesInt, secondsInt))
        elif "covert weight" in query:
            weightConverter()
        elif "tell" and "fact" in query:
            if __name__ == '__main__':
                main()

        elif 'exit' in query:
            speak("thank you sir")
            exit()
