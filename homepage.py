import tkinter
from tkinter import ttk
from tkinter import *
import os
import urllib.request
from updater import Updater

def playMultiOnl():
    name = "raceMultiSockets.py"
    os.system(name)

def playMultiOff():
    """"
    link = "https://raw.githubusercontent.com/dakinfemiwa/RacingGame/master/raceMultiplayerOffline.py"
    name = "raceMP.py"

    urllib.request.urlretrieve(link, name)

    x = os.getcwd()

    os.system("cd " + x)
    os.system(name)
    """
    name = "raceMultiplayerOffline.py"
    os.system(name)

def playSingular():
    """
    link = "https://raw.githubusercontent.com/dakinfemiwa/RacingGame/master/race.py"
    name = "raceP.py"

    urllib.request.urlretrieve(link, name)

    x = os.getcwd()

    os.system("cd " + x)
    """

    name = "race.py"
    os.system(name)

update = Updater()

playSingularText = "       PLAY SINGULAR       "
playMultiOffTxt = " PLAY MULTIPLAYER OFFLINE "
playMultiOnlTxt = " PLAY MULTIPLAYER ONLINE  "

homepageWindow = Tk()
homepageWindow.overrideredirect(1)
homepageWindow.title("RACERS")
homepageWindow.geometry("600x400+150+100")

photo = PhotoImage(file="raceFlag.png")
backgroundLabel = Label(homepageWindow, image=photo)
backgroundLabel.place(relx=.0, rely=.0)

playButton = Button(homepageWindow, text=playSingularText, bd=0, background="black", foreground="white", font="Ebrima 15", activebackground="gray", activeforeground="black", command=playSingular, width=25)
playButton.config(cursor="hand2")
playButton.place(relx=.275, rely=.35)

playButton1 = Button(homepageWindow, text=playMultiOffTxt, bd=0, background="black", foreground="white", font="Ebrima 15", activebackground="gray", activeforeground="black", command=playMultiOff, width=25)
playButton1.config(cursor="hand2")
playButton1.place(relx=.275, rely=.55)

playButton2 = Button(homepageWindow, text=playMultiOnlTxt, bd=0, background="black", foreground="white", font="Ebrima 15", activebackground="gray", activeforeground="black", command=playMultiOnl, width=25)
playButton2.config(cursor="hand2")
playButton2.place(relx=.275, rely=.75)

homepageWindow.mainloop()
