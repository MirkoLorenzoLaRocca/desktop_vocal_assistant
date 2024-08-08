import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import pyautogui
import time

# Inizializza il riconoscimento vocale e il motore di sintesi vocale
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Funzione per la sintesi vocale
def speak(text):
    print(f"Synthesizing speech: {text}")
    engine.say(text)
    engine.runAndWait()

def open_spotify():
    spotify_path = rf"C:\Users\mirko\AppData\Local\Microsoft\WindowsApps\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\Spotify.exe"
    print(f"Opening Spotify at {spotify_path}")
    os.startfile(spotify_path)

def open_whatsapp():
    whatsapp_path = rf"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2428.10.0_x64__cv1g1gvanyjgm\WhatsApp.exe"
    print(f"Opening WhatsApp at {whatsapp_path}")
    os.startfile(whatsapp_path)

def open_valorant():
    valorant_path = rf"C:\Riot Games\Riot Client\RiotClientServices.exe"
    os.startfile(valorant_path)

# Funzione per eseguire azioni basate sul comando vocale
def perform_action(command):
    if 'apollo' in command:
        speak("Sono Apollo, il Dio della musica")
        open_spotify()
        if 'suona' in command:
            time.sleep(5)
            pyautogui.press('space')
        if 'alza il volume' in command:
            for _ in range(2):  # Alza il volume di 2
                pyautogui.hotkey('ctrl', 'up')
                time.sleep(0.1)
        elif 'abbassa il volume' in command:
            for _ in range(2):  # Abbassa il volume di 2
                pyautogui.hotkey('ctrl', 'down')
                time.sleep(0.1)
    elif 'atena' in command:
        query = command.replace('atena', '').strip()
        url = f"https://www.google.com/search?q={query}"
        speak(f"Sono Atena, la Dea della conoscenza")
        webbrowser.open(url)
    elif 'ermes' in command:
        speak("Sono Ermes, il Dio messaggero")
        open_whatsapp()
    elif 'nike' in command:
        speak("Sono Nike, la Dea della vittoria")
        webbrowser.open("https://begamestar.it/")
    elif 'ares' in command:
        speak("Sono Ares, è tempo di andare in guerra")
        open_valorant()

# Funzione principale per il riconoscimento vocale
def listen_for_commands():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Sono in ascolto...")

        try:
            audio = recognizer.listen(source, timeout=1000, phrase_time_limit=5)
            command = recognizer.recognize_google(audio, language='it-IT')
            print(f"Hai detto: {command}")
            perform_action(command.lower())
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            speak("L'Olimpo al momento è chiuso")

# Ciclo principale
if __name__ == "__main__":
    speak("Benvenuto nell'Olimpo, mortale")
    while True:
        listen_for_commands()