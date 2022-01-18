#Simple 24hr python desktop widget for windows created by CloudGlitch [ https://github.com/CloudGlitch ]
from tkinter import *

from time import strftime

main = Tk()
main.overrideredirect(1)
main.geometry("350x100")

main.title('CloudGlitch Clock')

def min() :
 main.geometry("70x20")

def max() :
  main.geometry("350x100")

title = Label(main,text="CloudGlitch                               ", background = "#555", width = 100)
btn = Button(main, text = 'X', width=2 , bd=0 , bg="red", command = main.destroy)
btn1 = Button(main, text = '[]', width=2 , bd=0 , bg="#555", command = max)
btn2 = Button(main, text = '-', width=2 , bd=0 , bg="#555", command = min)

btn.place( x=0 , y=0)   
btn1.place( x=20 , y=0) 
btn2.place( x=40 , y=0) 
title.place(x=0 , y=0)

def clock():
	tick = strftime('%H:%M:%S %p')

	clock_label .config(text =tick)

	clock_label .after(1000, clock)

clock_label = Label(main, font =('Impact', 50), foreground = '#333')

clock_label.place( x=0 , y = 25)

clock()
main.mainloop()
