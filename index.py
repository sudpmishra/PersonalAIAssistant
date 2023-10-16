import pyttsx3
import openai
import os
import speech_recognition as sr
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
OPENAI_Key = os.getenv("OPENAI_KEY")

messages = [
    { "role": "user", "content": "You are a personized virtual chat asistant assistant named Friday. Please limit your answers to a sentance or two, no more than that. Always start your response with Sure Sir"}
]

def _get_time():
    # Get the current time
    current_time = datetime.now().time()

    # Define time ranges
    morning_start = datetime.strptime('06:00:00', '%H:%M:%S').time()
    afternoon_start = datetime.strptime('12:00:00', '%H:%M:%S').time()
    evening_start = datetime.strptime('18:00:00', '%H:%M:%S').time()
    night_start = datetime.strptime('00:00:00', '%H:%M:%S').time()

    # Check the current time and determine the part of the day
    if morning_start <= current_time < afternoon_start:
        part_of_day = "morning"
    elif afternoon_start <= current_time < evening_start:
        part_of_day = "afternoon"
    elif evening_start <= current_time < night_start:
        part_of_day = "evening"
    else:
        part_of_day = "night"
    return part_of_day

def _speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()

def _listen():
    recognizer = sr.Recognizer()
    while(True):
        # Open the microphone and start listening
        with sr.Microphone() as source:
            print("Say something:")
            audio = recognizer.listen(source)

        # Use a speech-to-text engine to convert audio to text
        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error connecting to the Google API: {0}".format(e))


def _get_gpt_response(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        max_tokens = 200,
        n = 1,
        stop = None,
        temperature = 0.5
    )
    message = response.choices[0].message.content
    print(message)
    messages = messages.append({"role": "assistant", "content": message})
    return message


shoutdown = False
while(not shoutdown):
    text = _listen()
    textLcase = text.lower()
    if('shut' in textLcase and 'down' in textLcase):
        print("Shutting down")
        _speak(f"Shutting down! Good {_get_time()} sir.")
        shoutdown = True
    else:
        messages.append({"role": 'user', "content": text})
        response = _get_gpt_response(messages, "gpt-4")
        _speak(response)

