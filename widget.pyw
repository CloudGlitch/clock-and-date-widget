from tkinter import *
import os
import datetime as dt
from time import strftime

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
main.bind('<Button-1>', SaveLastClickPos)
main.bind('<B1-Motion>', Dragging)
main.title("CloudGlitch | Lock Widget")
main.overrideredirect(1)
main.config(bg = 'grey')
main.wm_attributes("-transparentcolor", "grey")

app_width = 500	
app_height = 500
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

x = (screen_width / 2)  - (app_width / 2)
y = (screen_height / 2)  - (app_height / 2)

main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

def reset() :
 app_width = 500	
 app_height = 500
 screen_width = main.winfo_screenwidth()
 screen_height = main.winfo_screenheight()
 x = (screen_width / 2)  - (app_width / 2)
 y = (screen_height / 2)  - (app_height / 2)
 main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

def clock():
	tick = strftime(' %H:%M:%S %p')

	clock_label .config(text =tick)

	clock_label .after(1000, clock)



clock_label = Label(main, font =('Impact', 50),bg="grey", foreground = '#000')

clock_label.place(relx=0.5,rely=0.1,anchor=CENTER)

clock()

date = dt.datetime.now()
button = Button(main, text=f"{date: %a, %b %d,%Y}",bd=0,bg="grey", font="Impact, 18",fg="#000",command = reset)
button.place(relx=0.5,rely=0.2,anchor=CENTER)



main.mainloop()
