import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import requests
import musicLibrary
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

r = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def aiProcess(command):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=command,
        config=types.GenerateContentConfig(
            system_instruction="You are Jarvis, a short and helpful voice assistant. Answer in 1-2 sentences."
        ),
    )
    return response.text


def getWeather(country="Italy"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={country}&appid={WEATHER_API_KEY}&units=metric"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return f"It is {data['main']['temp']} degrees Celsius in {country} with {data['weather'][0]['description']}"
    print("Weather error:", res.status_code, res.text)
    return "Sorry, I could not get the weather"


def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open github" in c:
        webbrowser.open("https://github.com")
    elif "open email" in c:
        webbrowser.open("https://mail.google.com")
    elif "weather" in c or "temperature" in c:
        speak(getWeather())
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)    
    else:
        try:
            answer = aiProcess(c)
            print("Jarvis:", answer)
            speak(answer)
        except Exception as e:
            print("AI error;", repr(e))
            speak("Sorry, my AI is not available right now")


def listen_once(source, timeout, phrase_time_limit):
    """Returns recognized text, or None if nothing was understood."""
    try:
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        return r.recognize_google(audio)
    except (sr.WaitTimeoutError, sr.UnknownValueError):
        return None
    except Exception as e:
        print("error;", repr(e))
        return None


if __name__ == "__main__":
    speak("Initializing Jarvis")
    active = False

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)

        while True:
            if not active:
                print("Waiting for wake word...")
                word = listen_once(source, timeout=3, phrase_time_limit=3)
                if word and "jarvis" in word.lower():
                    speak("Yes sir")
                    active = True
                    print("Jarvis Activated.... (say 'stop listening' to sleep)")
            else:
                print("Listening for command...")
                command = listen_once(source, timeout=5, phrase_time_limit=8)
                if not command:
                    continue
                print("You said:", command)

                if "exit" in command.lower():
                    speak("Goodbye")
                    break
                elif "stop listening" in command.lower():
                    speak("Going to sleep")
                    active = False
                else:
                    processCommand(command)