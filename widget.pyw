#Simple 24hr python desktop widget for windows created by CloudGlitch [ https://github.com/CloudGlitch ]
from tkinter import *
import datetime as dt
from time import strftime
from webbrowser import *


lastClickX = 0
lastClickY = 0


def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    x, y = event.x - lastClickX + main.winfo_x(), event.y - lastClickY + main.winfo_y()
    main.geometry("+%s+%s" % (x , y))



main = Tk()
main.overrideredirect(1)
main.geometry("350x150")
main.geometry("+20+20")
main.bind('<Button-1>', SaveLastClickPos)
main.bind('<B1-Motion>', Dragging)

main.title('CloudGlitch Clock')

def min() :
 main.geometry("70x20")

def max() :
  main.geometry("350x150")

title = Label(main,text="CloudGlitch                                               ", background = "#555" , height=0, width = 100,font=('Arial',10))
btn = Button(main, text = 'X', width=2 , bd=0 ,height=1, bg="red", command = main.destroy)
btn1 = Button(main, text = '[]', width=2 , bd=0 ,height=1, bg="#555", command = max)
btn2 = Button(main, text = '-', width=2 , bd=0 ,height=1, bg="#555", command = min)

btn.place( x=0 , y=0)   
btn1.place( x=20 , y=0) 
btn2.place( x=40 , y=0) 
title.place(x=0 , y=0)

def clock():
	tick = strftime(' %H:%M:%S %p')

	clock_label .config(text =tick)

	clock_label .after(1000, clock)

clock_label = Label(main, font =('Impact', 50), foreground = '#333')

clock_label.place( x=0 , y = 25)

clock()
date = dt.datetime.now()
label = Label(main, text=f"{date: %A, %B %d, %Y}", font="Impact, 20")
label.place(x=0,y=100)
main.mainloop()
