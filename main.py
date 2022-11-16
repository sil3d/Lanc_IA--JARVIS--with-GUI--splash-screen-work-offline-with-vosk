from vosk import Model, KaldiRecognizer
import pyttsx3
import pyaudio
import msvcrt as m
import random
import os
import json
import datetime
import time
import webbrowser as web
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Lanc import Ui_Form
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from demarrage import Ui_Lanc

import pyautogui
## ==> GLOBALS
counter = 0
 

def wait():
    m.getch()
    
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
Lanc_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_V110_frFR_JulieM"
rate = engine.setProperty("rate",195)
engine.setProperty('voice', Lanc_id)


def speak(audio):
    print ("LANCE:" + str(audio)) #pour prototype 1
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("bonjour!! ")
    elif hour >= 12 and hour < 18:
        speak("bonne aprés midi!")
    elif hour >= 18 and hour < 23:
        speak('Bonsoir à vous!!')
    else :
        speak("il se fait tard, vous devriez allez vous couché")

    speak('je suis LANCE pour vous servir!')  
    speak("je suis toujours en mode écoute")
    speak("je vous écoute")
    print("..") 


model = Model("vosk-model-small-fr-0.22")
rec = KaldiRecognizer(model, 16000)
cap = pyaudio.PyAudio()
stream=cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        wishme()
    
        while True:
            
            data = stream.read(4000, exception_on_overflow=False)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = rec.Result()
                result = json.loads(result)
                print ("speaker: "+ result["text"])
                a = result["text"]
                f = open("name.txt", "r")
                

                if "comment tu vas" in a or "comment vas-tu" in a or "ça va toi" in a:
                    os.system('cls')
                    stream.stop_stream()
                    print('speaker: '+ str(a))
                    a = ["merci, je vais bien" ,"pas trop mal merci" ,"ça peux aller" ,"je n'ai pas vraiment d'émotions, mais ça peux aller" ]
                    speak(random.choice(a)) 
                    stream.start_stream()
                
                    print("...")
                    print('écoute...')
                elif 'bonjour' in a or 'salut' in a or 'hello'in a or 'coucou' in a :
                    os.system('cls')
                    stream.stop_stream()
                    print('speaker: '+ str(a))
                    speak('bonjour' + f.read())
                    speak("en quoi puis-je t'aider aujourdh'ui")
                    stream.start_stream()
                    print("...")
                    print('écoute...')
                elif "je t'admire" in a or "tu es tellement" in a:
                    reply_aime = ["Je sais", "j'apprécie votre sentiment", "merci c'est gentil", "ohh merci beaucoup", "vous de meme"]
                    os.system('cls')
                    stream.stop_stream()
                    print('speaker: '+ str(a))
                    speak(random.choice(reply_aime))
                    stream.start_stream()
                
                    print("...")
                    print('écoute...')
                elif "je vais bien" in a or "je vais bien " in a or "ça va" in a or 'ça peut aller' in a:
                    reply = ["tant mieux", "heureux de l'entendre", "cool alors", "super, et sinon comment je peux t'aider?", "ravis de l'entendre, et sinon comment puis-je t'aider?"] 
                    os.system('cls')
                    stream.stop_stream()
                    print('speaker: '+ str(a))
                    speak(random.choice(reply))
                    stream.start_stream()
                
                    print("...")
                    print('écoute...')
                elif "je ne vais pas bien" in a  or "bof" in a or "ça ne va pas bien" in a :
                    reply = ["pourquoi?" , "désolé pour toi" ] 
                    os.system('cls')
                    stream.stop_stream()
                    print('speaker: '+ str(a))
                    speak(random.choice(reply))
                    speak("je vous suggére d'allez prendre un peu d'air")
                    stream.start_stream()
                
                    print("...")
                    print('écoute...')
                
                elif "comment tu t'appelles" in a or "qui es-tu" in a or "qui" in a or "tu es" in a or "tu es qui" in a :
                    os.system('cls')
                    stream.stop_stream()
                    print('speaker: '+ str(a))
                    speak("je m'appelles LANCE")
                    speak("Concraitement je suis une IA je simule l'intelligence humaine")
                    speak("mais je ne suis pas autonome")
                    speak("mon role: assistant")
                    stream.start_stream()
                
                    print("...")
                    print('écoute...')
                elif "lanc" in a or "lance" in a or "debout" in a or "tu es là" in a or "tu es la" in a :
                    os.system('cls')
                    reply = ["toujours présent","oui, je suis là!!","hum hum","oui"]
                    stream.stop_stream()
                    print('speaker: '+ str(a))
                    speak(random.choice(reply))
                    speak("en quoi puis-je vous être  utile?")
                    stream.start_stream()
                
                    print("...")
                    print('écoute...')
                elif "Bonsoir lanc" in a or "Bonsoir lance" in a or "bonsoir" in a :
                    os.system('cls')
                    reply = ["Bonsoir!,j'éspère que vous avez passé une bonne journée!", "Bonsoir !, comment avez-vous passé la journée? j'éspère que vous n'étes pas trop fatiqué"]
                    stream.stop_stream()
                    print('speaker: '+ str(a))
                    speak(random.choice(reply))
                    stream.start_stream()
                
                    print("...")
                    print('écoute...')


startExecution = MainThread()


class Main(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.Start_pushButton.clicked.connect(self.startTask)
        self.ui.Stop_pushButton.clicked.connect(self.close)
        self.ui.hide_pushButton.clicked.connect(self.minimize)
        self.ui.user_pushButton.clicked.connect(self.save_text)

#..................SAVE........QLINE..................//
        
		
        
#..............WEB PAGE.......................//
        self.ui.Facebook_pushButton.clicked.connect(self.facebook)
        self.ui.Instagramm_pushButton_5.clicked.connect(self.instagram)
        self.ui.Tikitok_pushButton_4.clicked.connect(self.tiktok)
        self.ui.Google_pushButton_3.clicked.connect(self.google)
        self.ui.Youtube_pushButton_2.clicked.connect(self.youtube)
#..............VOLUME.....................//
        self.ui.volume_moins_push_button.clicked.connect(self.volume_moins)
        self.ui.Volume_plus_pushButton.clicked.connect(self.volume_up)
        self.ui.mute_push_button.clicked.connect(self.mute)

    def save_text(self):
        self.user_lineEdit = QLineEdit()
        text = self.user_lineEdit.text() 
        with open("name.txt", "w") as f:
            f.write(text)
        msg = QMessageBox()
        msg.setText('Utilisateur enrégistré, Appuyer sur Start')
        msg.exec_()
        
                
                
      
    def facebook(self):
        web.open("https://www.facebook.com/")

    def instagram(self):
        web.open("https://www.instagram.com/")

    def tiktok(self):
        web.open("https://www.tiktok.com/")

    def google(self):
        web.open("https://www.google.com/")

    def youtube(self):
        web.open("https://www.youtube.com/")

    def minimize(self):
        self.showMinimized()


    def volume_moins(self):
        pyautogui.press('volumedown')

    def volume_up(self):
        pyautogui.press('volumeup')
    
    def mute(self):
        pyautogui.press('volumemute')


    def startTask(self):
        self.ui.movie = QtGui.QMovie("Images/Gif/AI-visualization-design-unscreen.gif")
        self.ui.gif1.setMovie(self.ui.movie)
        self.ui.movie.start()
      
        startExecution.start()

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Lanc()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.description.setText("chargement du modéle")
        

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.description.setText("Un Instant"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.description.setText("Affichage de l'interface"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = Main()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

app = QApplication(sys.argv)
Lanc = SplashScreen()
exit(app.exec_())
