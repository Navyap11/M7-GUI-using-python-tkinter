from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Denomination Calculator")
window.configure(bg="light blue")
window.geometry("650x400")

upload = Image.open("img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(window, image=image, bg='light blue')
label.place(x=180, y=40)

intro_lbl= Label(text="Hey User! Welcome To Denomination Counter Application.")
intro_lbl.place(x=180, y=20)

def topwin():
    top=Toplevel()
    top.title("Top level window")
    top.configure(bg="light pink")
    top.geometry("600x350")

    ttl_amnt= Label(top, text="Enter total amount")
    ttl_amnt.place(x=230, y=50)

    ttl_entry= Entry(top)
    ttl_entry.place(x=220, y=80)

    ttl_btn= Button(top, text="Calculate")
    ttl_btn.place(x=250, y=120)

    result_lbl= Label(top, text="Here are the number of notes for each denomination")
    result_lbl.place(x=145, y=170)

    top.mainloop()

def new():
    msg= messagebox.showinfo("Alert!", "do you want to calculate the denomination count?")
    if msg=="ok":
        topwin()

intro_btn= Button(text="Let's Get Started", fg="white", bg="red", command= new)
intro_btn.place(x=260, y=360)

window.mainloop()

