from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("400x400")
window.title("Event Handler")

def handle_click(event):
    print("Button is clicked!")

button= Button(bg= "#243B3F", fg= "white", borderwidth= 1, text="Click me!")
button.pack()
button.bind("<Button-1>", handle_click)

def handle_key(event):
    print(event.char)

window.bind("<Key>", handle_key)

def message():
    messagebox.showwarning("Alert!", "stop, virus found!")

virus_btn= Button(bg= "#243B3F", fg= "white", borderwidth= 1, text="Scan for viruses", command= message)
virus_btn.place(x= 180, y=70)


window.mainloop()
