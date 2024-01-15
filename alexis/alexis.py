import pyttsx3
import datetime
import speech_recognition as sp
import wikipedia
import webbrowser
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from random import *
import random as rand
from time import ctime
import time
import pywhatkit as kit
import psutil  
import math
import pyjokes  
import requests, json
import smtplib
import pyautogui
from googlesearch import *



boolean = True
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
#print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1)

def takeCommand():
    r = sp.Recognizer()
    with sp.Microphone() as source:
        print("I am Listening.Try..")
       # speak("I am Listening... Ask Me anything....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        #print("Taking Inputs...")
        #speak("Taking inputs from my master")
        query = r.recognize_google(audio,language='en-in')
        print("Inputs: "+query+"\n")
       # speak(query)

    
    except Exception as e:
        print("Sorry Can you Please come again....")
        speak("Sorry Can you Please come again....")
        return "None"
    
    return query   


def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("done sir")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("good afternoon sir!")
    elif hour>18 and hour<21:
        speak("good evening sir!")
    else:
        speak("good night !")
   
#speak("My name is Alexis ,                 I am at your service sir!")

def wishme_end():
    
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    

def googleSearch(query):
    chrome_path = r'C:\\Program Files\\Google\\Chrome\\Application %s'
    for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
        webbrowser.open("https://google.com/search?q=%s" % query)
        
        
def screenshot():
    img = pyautogui.screenshot()
    img.save('C:\\Users\\manthan.pasare\\Desktop\\SS\\screenshot.png')
    speak('Screenshot captured')
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('manthanpasare844@gmail.com', 'Manthan@2307')
    server.sendmail('manthanpasare844@gmail.com', to, content)
    server.close()

def personal():
    speak(
        "I am Alexis,I am an AI assistent"
    )
    speak("Now i hope you know me")
    
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))

def weather():
    api_key = "9a53c5cbe11e9cf27dfceeb7d8cd2ce4" #generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("tell me which city")
    city_name = takeCommand()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        print(r)
        speak(r)
    else:
        speak(" City Not Found ")

def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)
    
def news():
    try: 
        jsonObj = urlopen('http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=e596a700dd134e7e8236d77b43f54406')
        data = json.load(jsonObj)
        i = 1	
        speak('here are some top news from the times of india')
        print('''=============== TIMES OF INDIA ============'''+ '\n')
        for item in data['articles']:
         print(str(i) + '. ' + item['title'] + '\n')
         print(item['description'] + '\n')
         speak(str(i) + '. ' + item['title'] + '\n')
         i += 1
    except Exception as e:
		   print(str(e)) 
    
    
def main():
       wishme()
       query= takeCommand().lower()
       if 'wikipedia' in query:
        speak('Searching in Wikipedia....')
        query= query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=5)
        speak("According to Wikipedia")
        print(results)
        speak(results)
      
           
       elif 'how are you' in query or 'and you' in query or 'what about you' in query or 'are you ok' in query: 
           speak('I am fine thank you,  Thanks for asking ')
       
       elif "calculate" in query:
        query = query.split(" ")
        if query[2]=="+":
            num1=query[1]
            num2=query[3]
            add=int(num1)+int(num2)
            str_add=str(add)
            speak("The answer is"+str_add)
            print(str_add)
        elif query[2]=="multiply":
            num1=query[1]
            num2=query[3]
            add=float(num1)*float(num2)
            str_mul=str(add)
            speak("The Required answer is " + str_mul)
            print(str_mul)
        elif query[1]=="factorial":
            fac=math.factorial(int(query[3]))
            str_fac=str(fac)
            speak(str_fac)
            print(str_fac)

       elif ("tell me about yourself" in query):
            personal()
       elif ("about you" in query):
            personal()
       elif ("who are you" in query):
            personal()
       elif ("yourself" in query):
            personal()
            
            
       elif 'open youtube' in query:
        speak('opening youtube please wait...')
        webbrowser.open("youtube.com")
        
       elif 'screenshot' in query:
          screenshot()
        
     
       elif 'google' in query:
        speak('Searching on google...')
        #webbrowser.open("google.com")
        query= query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to google")
        print(results)
        speak(results)
       
       elif 'news' in query:
         news()
       
       elif 'song' in query or 'music' in query:
         speak('Playing the required song on youtube')
         kit.playonyt(query)
         
       elif 'open facebook for me' in query:
        speak('opening facebook please wait for a moment...')
        googleSearch('https://www.facebook.com/manthan.pasare.9')
        
       
       elif 'search' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chromium').open_new_tab(
                url)
            speak('Here is What I found for' + search)

       elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)
        
       elif 'the time' in query:
        hour=int(datetime.datetime.now().hour)
        strtime = datetime.datetime.now().strftime("%H:%M")
        if hour>24 and hour<12:
            speak("The good time is "+strtime+"am")
            print(strtime+ "am") 
        elif hour>12 and hour<24:
            speak("The good time is "+strtime+"pm")
            print(strtime+ "pm")
        
       elif "check my internet connection"in query or "check internet connection" in query:
        hostname="google.co.in"
        response=os.system("ping -c 1"+hostname)
        if response==0:
            speak("I Think Internet is Disconnected")
        else:
            speak("Internet Connection is fine Sir")
            
            
       elif ("cpu and battery" in query or "battery" in query
              or "cpu" in query):
            cpu()


       elif ("tell me a joke" in query or "joke" in query):
            jokes()
     
            
       elif 'good job' in query:
         speak("I Learnt from my Master buddy...")
         
       elif ("weather" in query or "temperature" in query):
            weather()
         
       elif "what time is it" in query:
        print(ctime())
        speak(ctime()) 
        
       elif ("voice" in query):
            speak("for female say female and, for male say male")
            q = takeCommand()
            if ("female" in q):
                voice_change(1)
            elif ("male" in q):
                voice_change(0)
       elif ("male" in query or "female" in query):
            if ("female" in query):
                voice_change(1)
            elif ("male" in query):
                voice_change(0)
                
       elif 'volume' in query:
           speak("Tell me how much should be the volume")
           q = takeCommand()
           volume_set()
           
       elif "will you be my gf" in query or "will you be my bf" in query:   
            speak("I'm not sure about, may be you should give me some time")
 
       elif "how are you" in query:
            speak("I'm fine, glad you me that")
 
       elif "i love you" in query:
            speak("It's hard to understand")    
       
       elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('demo.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = ctime()
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('Note added successfully')
            else:
                file.write(note)
         
       elif "show note" in query:
            speak("Showing Notes")
            file = open("demo.txt", "r") 
            print(file.read())
            speak(file.read(6))     
       
       elif ("tell me your powers" in query or "help" in query
              or "features" in query):
            features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can tell you battery and cpu usage,
            i can take screenshots,
            i can send email to your boss or family or your friend,
            i can shut down or logout or hibernate your system,
            i can tell you non funny jokes,
            i can open any website,
            i can search the thing on wikipedia,
            i can change my voice from male to female and vice-versa
            And yes one more thing, My boss is working on this system to add more features...,
            tell me what can i do for you??
            '''
            print(features)
            speak(features)
            
       elif 'send email' in query or 'send an email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sumbechinmay10@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
            
       else:
        googleSearch(query)
        
        
while boolean:
    query= takeCommand().lower() 
    if 'alexis' in query:
        #elif 'hey alexis' in query or'hello assistant' in query:
     rand=randint(1,5)
     if rand==1:
            speak(" I am at your service sir!            Yes tell me what to do")
     if rand==2:
            speak("Ask me anything")
     if rand==3:
            speak("Yes sir! What can I do for you ?")
     if rand==4:
            speak("Yes My Master How are you! what is my task")
     if rand==5:
            speak("yes please tell me the query")
        
        #speech = get_audio()
        #print(speech)
     main()
        
    elif 'sleep' in query or 'shutup' in query:
        wishme_end()
        speak("Bye Bye . Have a nice day         closing in 3, 2, 1, 0 seconds")
        boolean = False
        break    
      

                