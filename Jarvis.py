import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui
import smtplib
import psutil
import pyjokes


email={"Rahul":"demo@gmail.com"} #provide emails with their names to send the email when they said their names

def speak(str):
    '''
    It is a function which speak the words which are pass through it.
    '''
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    speed_voice_rate=150
    engine.setProperty('rate',speed_voice_rate)
    engine.say(str)
    engine.runAndWait()


def wishme():
    '''It takes time and according to the time it wishes you'''
    time = int(datetime.datetime.now().strftime('%H'))
    if time >= 6 and time < 12:
        speak("Good Morning")
    elif time >= 12 and time < 18:
        speak("Good Afternoon")
    elif time >= 18 and time < 21:
        speak("Good Evening")
    else:
        speak("Its too late you must sleep")


def getCommand():
    '''It listens what you said and returns in string format'''
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}")
        return query

    except Exception as e:
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"

def sendEmail(to,content):
    ''' It takes the sending email that you want to sent the message and it takes the content which you want to send it'''
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('demoversion54@gmail.com','******') #provide your email and password 
    server.sendmail('demoversion54@gmail.com',to,content)
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save("F:\Git Work\Python-Codes\Python Projects\SS.png")

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery=psutil.sensors_battery()
    speak("battery percentage is")
    speak(battery.percent)

if __name__ == "__main__":
    speak("Welcome back sir")
    wishme()
    speak("Jarvis at your service. How can I help you?")

    while True:
        query=getCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia Please wait")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "search" in query:
            statement=query.replace("search","")
            webbrowser.open_new_tab(statement)


        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "time" in query:
            time=datetime.datetime.now().strftime("%I:%M. %p")
            speak(time)

        elif "thank you" in query:
            speak("Welcome Sir.")

        elif "play music" in query:
            speak("Which song do you want to listen?")
            query=getCommand().lower()
            location = "F:\\Music"
            music = os.listdir(location)
            for songs in music:
                if query in songs.lower():
                    os.startfile(os.path.join(location,songs))

        elif "open code" in query:
            location="C:\\Users\\Pratik\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(location)

        elif "send email" in query:
            try:
                speak("Please say the name for whom do you want to sent the e-mail")
                name=getCommand().lower()
                for i in email.items():
                    if name in i:
                        to=(i[1])
                        speak("Please say the content you want to send")
                        content=getCommand()
                        sendEmail(to,content)
                        speak("Email has been sent successfully.")
                    else:
                        speak("Name is not in the list")

            except Exception as e:
                print(e)
                speak("Something error has occured")

        elif "screenshot" in query:
            screenshot()
            speak("Screenshot is taken")

        elif "battery" in query:
            cpu()

        elif "jokes" in query:
            speak(pyjokes.get_joke(language='en'))

        elif "shutdown" in query:
            speak("Thank you sir. Jarvis is shutting down.")
            break



