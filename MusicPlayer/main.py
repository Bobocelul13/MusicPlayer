import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Joac-o, Leila, Leila")
    mixer.music.play()

def pausesong():
    songstatus.set("Stop, PAUZAAAAAAAA")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stop, pana, a picat curentul")
    mixer.music.stop()

def resumesong():
    songstatus.set("Joac-o, Leila")
    mixer.music.unpause()    

root=Tk()
root.title('Boboc-inatorul')

mixer.init()
songstatus=StringVar()
songstatus.set("Hai odata, alege")

#playlist---------------

playlist=Listbox(root,selectmode=SINGLE,bg="Red",fg="white",font=('arial',15),width=100, height=30)
playlist.grid(columnspan=5)

os.chdir(r'C:\Coade\MusicPlayer\music')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="Joac-o, Leila, Leila",command=playsong)
playbtn.config(font=('arial',20),bg="Black",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Stop, PAUZAAAAAAAA",command=pausesong)
pausebtn.config(font=('arial',20),bg="Black",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="Stop, pana, a picat curentul",command=stopsong)
stopbtn.config(font=('arial',20),bg="Black",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="Joac-o, Leila",command=resumesong)
Resumebtn.config(font=('arial',20),bg="Black",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)

mainloop()