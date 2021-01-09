# from tkinter import *
# import PIL.Image,PIL.ImageTk
from PIL import Image
import speech_recognition as sr
import pyttsx3
import datetime
import time
import os
import pyjokes
import wikipedia
import webbrowser
from cv2 import cv2  #pip install opencv-python
import pyautogui
import random
import ctypes
import subprocess
import winshell
#from PIL import Image

# window=Tk()
# window.title("ELZA")
# window.geometry('1000x500')
# window.configure(bg="black")
# #img=ImageTk.PhotoImage(Image.open(r"C:/Users/ANUSHA/Desktop/MINI project/images/anu.jpg"))
# global var
# global var1
# var=StringVar()
# var1=StringVar()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        # var.set('Good Morning')
        # window.update()
        speak("Good Morning !")

    elif hour >= 12 and hour < 16:
        # var.set('Good Afternoon')
        # window.update()
        speak("Good Afternoon  !")

    else:
        # var.set('Good Evening !')
        # window.update()
        speak("Good Evening !")
   
    assname = ("elza")
    speak("I am your Assistant")
    speak(assname)
    

def takeCommand():              

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        # print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query

if __name__ == '__main__':
    def clear(): return os.system('cls')
    clear()
        # This Function will clean any
    # command before execution of this python file
    
    wishMe()
    speak("What should i call you ")
    uname = takeCommand()
    speak("Welcome ")
    speak(uname)
    print("Welcome", uname)
    speak("How can i Help you ")
    assname="elza"
    while True:

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        #GENERAL QUESTIONS
        if 'hey' in query or 'hi' in query or 'hai' in query or 'hello' in query:
            speak("hello")
            speak(uname)
            speak("Tell me what can i do for u")
        
        elif 'tasks' in query:
            speak("i can do :")
            
        elif "who are you" in query:
            # var.set('I am your virtual assistant created by ANUSHA')
            # window.update()
            speak("I am your virtual assistant created by ANUSHA")

        elif "elsa" in query:
            wishMe()
            speak("ELZA IS IN YOUR SERVICE")
            #speak("")

        elif 'how are you' in query:
            speak("I am fine, glad you ask me that")
            speak("How are you, Sir")

        elif 'fine' in query or " i am good" in query:
            speak("It's good to know that your fine")
 
        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Miss Anusha ")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Anusha.")

        elif "Morning" in query:
            speak("A warm Morning")
            speak("How are you")
            speak(uname)

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
 
            #launching social media applications
        elif 'youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")


        elif 'google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'stack overflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "C:\\Users\\ANUSHA\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))
        
        elif 'take a photo' in query:
            cam = cv2.VideoCapture(0)
            #establishes  the camera --laptop camera port=0
            print("capturing face...")
            count=random.randint(0,1000)

            while True:
                ret, img = cam.read()

                cv2.imshow("Test", img)

                if not ret:
                    break

                k=cv2.waitKey(1)

                if k%256==27:
                    #For Esc key
                    print("Close")
                    print("photo taken")
                    break
                elif k%256==32:
                    #For Space key

                    print("Image "+str(count)+"saved")
                    file='C:/Users/ANUSHA/Desktop/MINI project/images/img'+str(count)+'.jpg'
                    cv2.imwrite(file, img)
                    

            cam.release
            cv2.destroyAllWindows
        
        elif 'screenshot' in query:
            count=random.randint(0,1000)
            save='C:/Users/ANUSHA/Desktop/MINI project/images/screenshot'+str(count)+'.jpg'
            pyautogui.screenshot(save)
            print("took screenshot")

            # searching query in utube,google,wikipedia
        elif 'search' in query and 'youtube' in query:
            speak('Searching Youtube...')
            query = query[1]
            webbrowser.open('https://www.youtube.com/results?search_query='+query)

        
        elif 'search' in query and 'google' in query:
            speak('Searching Google...')
            query = query[1]
            webbrowser.open('https://google.com/?#q'+query)
        
        
        
        elif 'search' in query and 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('elza.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("elza.txt", "r") 
            print(file.read())
            speak(file.read(6))

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            os.system('shutdown /s /t 1') #  also os.system('shutdown -s')
        
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop elza from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google.nl / maps / place/" + location + "")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        
        elif 'exit' in query or "quit" in query or "goodbye" in query or "signingoff" in query or "bye" in query:
            speak("Thanks for giving me your time")
            exit()

# def update(ind):
#     frame = frames[(ind)%100]
#     ind += 1
#     label.configure(image=frame)
#     window.after(100, update, ind)

# label2 = Label(window, textvariable = var1, bg = '#FAB60C')
# label2.config(font=("Courier", 20))
# var1.set('User Said:')
# label2.pack()

# label1 = Label(window, textvariable = var, bg = '#ADD8E6')
# label1.config(font=("Courier", 20))
# var.set('Welcome')
# label1.pack()

# frames = [PhotoImage(file='C:/Users/ANUSHA/Desktop/MINI project/images/anu.jpg',format = 'jpg -index %i' %(i)) for i in range(100)]
# window.title('ELZA')

# label = Label(window, width = 500, height = 500)
# label.pack()
# window.after(0, update, 0)

# btn0 = Button(text = 'WISH ME',width = 20, command = wishMe, bg = '#5C85FB')
# btn0.config(font=("Courier", 12))
# btn0.pack()
# btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
# btn1.config(font=("Courier", 12))
# btn1.pack()
# btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
# btn2.config(font=("Courier", 12))
# btn2.pack()


# window.mainloop()







            #location, searching in google utube,wikipedia
            # appliaction search ,face recogntion
            #authentication key, language translator, comunicating in 3 languages
            #send mail,read selected text,alarms,remainders,time preditcion,weather
            #UI for elza