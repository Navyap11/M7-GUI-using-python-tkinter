from tkinter import *

window= Tk()
window.title("Length conversion")
window.geometry("400x300")

def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    textt= "cm: "+str(cm)
    label.config(text=textt)

title_label= Label(window, text="Enter length in inches:", bg= "#243B3F", fg= "white", borderwidth= 1)
title_label.pack()

entry = Entry(window)
entry.pack()

label = Label(window, text="")
label.pack()

button= Button(window, text="Convert", command=convert, bg= "#32646D", fg= "white")
button.pack()

window.mainloop()