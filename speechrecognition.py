import speech_recognition as sr
import psutil
import os

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized command: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return None

def close_app_by_name(app_name):
    found = False
    for process in psutil.process_iter(['pid', 'name']):
        if app_name.lower() in process.info['name'].lower():
            os.system(f"taskkill /F /PID {process.info['pid']}")
            print(f"Closed {process.info['name']}")
            found = True
    if not found:
        print(f"Application '{app_name}' not found.")

def list_running_processes():
    print("Running processes:")
    for process in psutil.process_iter(['pid', 'name']):
        print(f"Process: {process.info['name']}, PID: {process.info['pid']}")

if __name__ == "__main__":
    list_running_processes()  # Check the running processes before testing
    command = listen_for_command()
    if command:
        if "your command" in command: #change "your command" for whatever you want to say for it to execute
            close_app_by_name("chrome") #you can change app by typing app name ex:- chrome
        elif "your command" in command:
            close_app_by_name("chrome")
        elif "your command" in command:
            close_app_by_name("chrome")
        elif "your command" in command:
            close_app_by_name("chrome")
        else:
            print("No recognized application to close.")
