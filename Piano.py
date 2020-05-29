from tkinter import *
from pygame import mixer
root = Tk()
root.geometry('500x200')
root.title("Piano")

mixer.init()


def C():
    mixer.music.load("C.mp3")
    mixer.music.play()
def Db():
    mixer.music.load("C#.mp3")
    mixer.music.play()
def D():
    mixer.music.load("D.mp3")
    mixer.music.play()
def Eb():
    mixer.music.load("D#.mp3")
    mixer.music.play()
def E():
    mixer.music.load("E.mp3")
    mixer.music.play()
def F():
    mixer.music.load("F.mp3")
    mixer.music.play()
def Gb():
    mixer.music.load("F#.mp3")
    mixer.music.play()
def G():
    mixer.music.load("G.mp3")
    mixer.music.play()
def Ab():
    mixer.music.load("G#.mp3")
    mixer.music.play()
def A():
    mixer.music.load("A.mp3")
    mixer.music.play()
def Bb():
    mixer.music.load("A#.mp3")
    mixer.music.play()
def B():
    mixer.music.load("B.mp3")
    mixer.music.play()
def C2():
    mixer.music.load("C2.mp3")
    mixer.music.play()
def Db2():
    mixer.music.load("C#2.mp3")
    mixer.music.play()
def D2():
    mixer.music.load("D2.mp3")
    mixer.music.play()
def Eb2():
    mixer.music.load("D#2.mp3")
    mixer.music.play()
def E2():
    mixer.music.load("E2.mp3")
    mixer.music.play()
def F2():
    mixer.music.load("F2.mp3")
    mixer.music.play()
def Gb2():
    mixer.music.load("F#2.mp3")
    mixer.music.play()

b = Button(root, height=10, width=5, command=C, bg="white")
b.grid(row=0,column=1)

b2 = Button(root, height=10, width=5, command=D, bg="white")
b2.grid(row=0,column=2)

b3 = Button(root, height=10, width=5, command=E, bg="white")
b3.grid(row=0,column=3)

b4 = Button(root, height=10, width=5, command=F, bg="white")
b4.grid(row=0,column=4)

b5 = Button(root, height=10, width=5, command=G, bg="white")
b5.grid(row=0,column=5)

b6 = Button(root, height=10, width=5, command=A, bg="white")
b6.grid(row=0,column=6)

b7 = Button(root, height=10, width=5, command=B, bg="white")
b7.grid(row=0,column=7)

b8 = Button(root, height=10, width=5, command=C2, bg="white")
b8.grid(row=0,column=8)

b9 = Button(root, height=10, width=5, command=D2, bg="white")
b9.grid(row=0,column=9)

b10 = Button(root, height=10, width=5, command=E2, bg="white")
b10.grid(row=0,column=10)

b11 = Button(root, height=10, width=5, command=F2, bg="white")
b11.grid(row=0,column=11)

a1 = Button(root, command=Db, width=2, height=6, bg="black")
a1.place(x=32,y=0)

a2 = Button(root, command=Eb, width=2, height=6, bg="black")
a2.place(x=77,y=0)

a3 = Button(root, command=Gb, width=2, height=6, bg="black")
a3.place(x=167,y=0)

a4 = Button(root, command=Ab, width=2, height=6, bg="black")
a4.place(x=213,y=0)

a5 = Button(root, command=Bb, width=2, height=6, bg="black")
a5.place(x=257,y=0)

a6 = Button(root, command=Db2, width=2, height=6, bg="black")
a6.place(x=347,y=0)

a7 = Button(root, command=Eb2, width=2, height=6, bg="black")
a7.place(x=393,y=0)

a8 = Button(root, command=Gb2, width=2, height=6, bg="black")
a8.place(x=478,y=0)

    
    


root.mainloop()
