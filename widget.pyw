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
main.geometry("350x140")
main.geometry("+20+20")
main.bind('<Button-1>', SaveLastClickPos)
main.bind('<B1-Motion>', Dragging)

main.title('CloudGlitch Clock And Date Widget')

def more() :
 main.geometry("350x240")

def less() :
 main.geometry("350x140")

def about() :
 aboutWindow = Toplevel(main)
 
 aboutWindow.title("Simple Clock and Date Widget")
 aboutWindow.geometry("+20+200")
 aboutWindow.geometry("500x50")
 
 Label(aboutWindow,text ="Simple Clock and Date python desktop widget for windows created by CloudGlitch").pack()
 Label(aboutWindow,text ="Github :- https://github.com/CloudGlitch").pack()
 
btn = Button(main, text = '[]', width=2 , bd=0 ,height=1, command = more)
btn1 = Button(main, text = '-', width=2 , bd=0 ,height=1, command =  less)
close = Button(main, text = 'Close Widget' , bd=0,bg="grey",height=3 ,width=20,command = main.destroy)
about = Button(main, text = 'About' , bd=0,bg="grey",height=3 ,width=20,command  = about)

btn.place( x=0 , y=0)   
btn1.place( x=20 , y=0)
close.place( x = 20 , y = 150)
about.place( x=180,y=150)

def clock():
	tick = strftime(' %H:%M:%S %p')

	clock_label .config(text =tick)

	clock_label .after(1000, clock)

clock_label = Label(main, font =('Impact', 50), foreground = '#333')

clock_label.place( x=0 , y = 20)

clock()
date = dt.datetime.now()
label = Label(main, text=f"{date: %A, %B %d, %Y}", font="Impact, 20")
label.place(x=0,y=100)
main.mainloop()