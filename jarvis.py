import datetime
from re import search
import webbrowser
import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia

#shortcut for reloading ctrl shiift p commnd pallette then windows reload
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
     speak("Good Morning Sir have a good day!")


    elif hour>=12 and hour<17:
     speak("Good Afternoon Sir ")

    else:
        speak("Good Evening Sir, How may I help you?")

    # speak("whatsup")

def takeCommand():

    

    r = sr.Recognizer()
    with sr.Microphone() as source:
     print("Listening...")
     audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

   

    except Exception as e:
        print("Sorry , did not catch that") 
    return query     



if __name__=="__main__":
    wishMe()
    while True:
         query = takeCommand().lower()
       
         if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
         elif 'open netflix' in query:
             webbrowser.open("https://www.netflix.com/browse") 

         elif 'open youtube' in query:
             webbrowser.open("youtube.com")       

         elif 'weather'in query:
             speak("Showing the weather")
             webbrowser.open("https://www.accuweather.com/en/in/bengaluru/204108/weather-forecast/204108")

         elif "who are you" in query:
             with open("C:\\Users\\User\\Documents\\jarvis.txt") as f:
                contents = f.readlines()
                speak(contents)
         elif "instagram" in query:
             speak("Opening Instagram")
             webbrowser.open("instagram.com")
            
         elif 'thank you'in query:
            speak("You're Welcome")
            break
