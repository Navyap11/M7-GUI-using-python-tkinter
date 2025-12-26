from tkinter import *
from datetime import date

window = Tk()
window.geometry("400x400")
window.title("Age Calculator")

Label(window, text="Day").grid(row=0, column=0)
d = Entry(window)
d.grid(row=0, column=1)

Label(window, text="Month").grid(row=1, column=0)
m = Entry(window)
m.grid(row=1, column=1)

Label(window, text="Year").grid(row=2, column=0)
y = Entry(window)
y.grid(row=2, column=1)

result = Label(window, text="Age:")
result.grid(row=3, column=0, columnspan=2)

def age():
    today = date.today()
    a = today.year - int(y.get())
    if (today.month, today.day) < (int(m.get()), int(d.get())):
        a -= 1
    result.config(text="Age: " + str(a))

Button(window, text="Calculate", command=age).grid(row=4, column=0, columnspan=2)

window.mainloop()
