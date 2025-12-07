#lesson 1- widgets for starters
#activity 1: demonstration of tkinter window


#from tkinter import *

#window= Tk()
#window.title("tkinter window")
#window.geometry("400x300")
#window.mainloop()


# activity 2: first tkinter application

from tkinter import *

window= Tk()
window.title("tkinter window")
window.geometry("400x300")

greeting_label= Label(text="Hey There!", fg="white", bg="black", height=1, width=100)
name_label= Label(text="Full Name", fg="red", bg="white")
name_entry= Entry()
greeting_label.pack()
name_label.pack()
name_entry.pack()

def display():
    name = name_entry.get()
    message = "Welcome to the Application! "
    text_box.insert(END, message)
    text_box.insert(END, name)

button= Button(text="begin",command= display, height=1, bg= "#9456C7", fg="black")
button.pack()

text_box= Text(height=3)
text_box.pack()

window.mainloop()