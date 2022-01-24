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
main.wm_attributes("-transparentcolor", "#fff")
main.title('CloudGlitch Clock And Date Widget')


 

def more() :
 main.geometry("350x350")

def less() :
 main.geometry("350x140")

def reset() :
 main.geometry("+500+100")
 main.geometry("350x140")
 main.wm_attributes("-transparentcolor", "#fff")

def about() :
 aboutWindow = Toplevel(main)
 aboutWindow.title("Simple Clock and Date Widget")
 aboutWindow.geometry("+180+500")
 aboutWindow.geometry("1000x100")
 Label(aboutWindow,text ="Simple Clock and Date desktop widget for windows created by CloudGlitch").pack()
 Label(aboutWindow,text="For any help kindly visit this page -> https://github.com/CloudGlitch/clock-and-date-widget/issues").pack()
 Label(aboutWindow,text="version : you are running the latest version 2.2").pack()
 Label(aboutWindow,text ="Github :- https://github.com/CloudGlitch").pack()

def bg() :
 main.wm_attributes("-transparentcolor", "#add123")
 
more = Button(main, text = '▼',command = more,bd=0,bg="#fff").place(x=0,y=0)
close = Button(main, text = 'Close Widget' ,bg="grey",  bd=0,height=3 ,width=20,command = main.destroy)
about = Button(main, text = 'About' ,bg="grey",  bd=0,height=3 ,width=20,command = about)
reset = Button(main, text = 'Reset Widget' ,bg="grey",  bd=0,height=3 ,width=20,command = reset)
bg = Button(main, text = 'Show Background' ,bg="grey",  bd=0,height=3 ,width=20,command = bg)
less = Button(main, text = 'hide more menu',command = less,bd=0,bg="grey",width=43,height=2).place(x=20,y=290)

close.place( x = 20 , y = 150)
about.place( x=180,y=150)
reset.place(x=20,y=220)
bg.place(x=180,y=220)

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
