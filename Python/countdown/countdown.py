from tkinter import *
from tkinter import ttk 
from tkinter import font
import time
import datetime

global endTime

def quit(*args):
    root.destroy()


def count_down():
    timeLeft = endTime - datetime.datetime.now()
    timeLeft = timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)

    txt.set(timeLeft)
    root.after(1000, count_down)


root = Tk()
root.attributes('-fullscreen', False)
root.configure(background='black')
root.bind('x', quit)
root.after(1000, count_down)

endTime = datetime.datetime(2020, 12, 25, 0, 0)


fnt = font.Font(family='Helvetica', size=90, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()