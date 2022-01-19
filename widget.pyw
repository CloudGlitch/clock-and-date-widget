from tkinter import *
import tkinter as tk 
from tkinter import ttk
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
main.geometry("350x140")
main.geometry("+500+100")
main.bind('<Button-1>', SaveLastClickPos)
main.bind('<B1-Motion>', Dragging)
main.config(bg = '#ffffff')
main.wm_attributes('-transparentcolor','#ffffff')
main.title('CloudGlitch Clock And Date Widget')

def more() :
 main.geometry("350x270")

def less() :
 main.geometry("350x140")

def reset() :
 main.geometry("+500+100")
 main.geometry("350x140")

def about() :
 aboutWindow = Toplevel(main)
 
 aboutWindow.title("Simple Clock and Date Widget")
 aboutWindow.geometry("+20+200")
 aboutWindow.geometry("500x50")
 
 Label(aboutWindow,text ="Simple Clock and Date python desktop widget for windows created by CloudGlitch").pack()
 Label(aboutWindow,text ="Github :- https://github.com/CloudGlitch").pack()
 
btn = Button(main, text = '[]', width=2 ,bg="grey", bd=0 ,height=1 ,command = more)
btn1 = Button(main, text = '-', width=2 ,bg="grey",  bd=0 ,height=1, command =  less)
close = Button(main, text = 'Close Widget' ,bg="grey",  bd=0,height=3 ,width=20,command = main.destroy)
about = Button(main, text = 'About' ,bg="grey",  bd=0,height=3 ,width=20,command = about)
reset = Button(main, text = 'Reset Position' ,bg="grey",  bd=0,height=2 ,width=43,command = reset)

btn.place( x=0 , y=0)   
btn1.place( x=20 , y=0)
close.place( x = 20 , y = 150)
about.place( x=180,y=150)
reset.place(x=20,y=220)

def clock():
	tick = strftime(' %H:%M:%S %p')

	clock_label .config(text =tick)

	clock_label .after(1000, clock)

clock_label = Label(main, font =('Impact', 50),bg="#ffffff", foreground = '#000')

clock_label.place( x=0 , y = 20)

clock()
date = dt.datetime.now()
label = Label(main, text=f"{date: %A, %B %d, %Y}",bg="#ffffff", font="Impact, 20",fg="#000")
label.place(x=0,y=100)
main.mainloop()