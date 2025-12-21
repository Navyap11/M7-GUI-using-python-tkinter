from tkinter import *

window= Tk()
window.title("tkinter window")
window.geometry("400x300")

greeting_label= Label(text="Please input two numbers", fg="white", bg="black", height=1, width=100)
number1= Label(text="number 1.", fg="red", bg="white")
number1_entry= Entry(window)
number2= Label(text="number 2.", fg="red", bg="white")
number2_entry= Entry(window)
greeting_label.pack()
number1.pack()
number1_entry.pack()
number2.pack()
number2_entry.pack()

def display():
    num1 = int(number1_entry.get()) 
    num2= int(number2_entry.get())
    product= num1*num2
    message = "the product of the two numbers is: "+str(product) + "\n"
    text_box.insert(END, message)

button= Button(text="answer",command= display, height=1, bg= "#9456C7", fg="black")
button.pack()

text_box= Text(height=3)
text_box.pack()

window.mainloop()