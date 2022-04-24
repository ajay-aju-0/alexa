import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

login = {
    'ajay':'ajay123',
    'amal':'amal123',
    'sree':'sree123',
}

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[2].id)
engine.setProperty("voice",voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    

#it takes microphone commands from user and return string output
def takeCommand():
    reg = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        reg.pause_threshold = 1
        reg.energy_threshold = 2000
        audio = reg.listen(source)

    try:
        print("recognizing....")
        query = reg.recognize_google(audio,language="en-in")
        print(f"user said:{query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"

    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("ajaypadmanabhan01@gmail.com","password")
    server.sendmail("ajaypadmanabhan01@gmail.com",to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    user = ""
    speak("hello sir,please enter username")
    uname = input("username:")
    if uname in login:
        for i in range(3):
            speak("please enter password")
            passw = input("password:")

            if login[uname] == passw:
                user = "authenticated"
                break
            else:
                speak("password incorrect, please enter a valid password")
        # print(uname,passw,user)
        if user == "authenticated":
            ch = "y"
            speak("i am alexa sir ,Please tell me how can i help you")
            # while True:
            while ch == 'Y' or ch == 'y':
                query = takeCommand().lower()

                #logic for executing task based on query
                if 'wikipedia' in query:
                    print("searching wikipedia....")
                    speak("searching wikipedia....")
                    query = query.replace("wikipedia","")
                    results = wikipedia.summary(query,sentences=5)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")
                
                elif 'play music' in query:
                    music_dir = '.\music'
                    songs = os.listdir(music_dir)
                    # print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))

                elif 'the time' in query:
                    strtime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"sir,the time is:{strtime}\n")

                elif 'open code' in query:
                    codepath = "C:\\Users\\ajayaju\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codepath)

                elif 'open wordpad' in query:
                    codepath = "C:\\Windows\\WinSxS\\amd64_microsoft-windows-wordpad_31bf3856ad364e35_10.0.22000.1_none_83fe16d971ae9831\\wordpad.exe"
                    os.startfile(codepath)

                elif 'open microsoft word' in query:
                    codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                    os.startfile(codepath)

                elif 'open powerpoint' in query:
                    codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                    os.startfile(codepath)

                elif 'open notepad' in query:
                    codepath = "C:\\Windows\\notepad.exe"
                    os.startfile(codepath)

                elif 'email to me' in query:
                    try:
                        speak("what should i say...")
                        content = takeCommand()
                        to = "ajaypadmanabhan01@gmail.com"
                        sendEmail(to,content)
                        speak("email has been send successfully!")
                    except Exception as e:
                        speak("sorry sir.... you cant send an email at this moment")
                elif 'shut down' in query or 'shutdown' in query:
                    speak("shutting down alexa")
                    exit(0)

                ch = input("Do you want to continue,if yes press 'y':")
        else:
            speak("password is incorrect,i am not able to authenticate you")
            exit(0)
    else:
        speak("You are not an authenticated user, No user is present in that name")
        exit(0)