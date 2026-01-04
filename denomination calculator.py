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
    value= Entry(top)
    value.place(x=220, y=80)
    
    result_lbl= Label(top, text="Here are the number of notes for each denomination")
    result_lbl.place(x=145, y=170)

    tthousand_lbl= Label(top,text="2000")
    tthousand_lbl.place(x=180, y=200)
    t1= Entry(top)
    t1.place(x=270, y=200)

    fhundred_lbl= Label(top, text="500")
    fhundred_lbl.place(x=180, y=230)
    t2= Entry(top)
    t2.place(x=270, y=230)

    hundred= Label(top, text="100")
    hundred.place(x=180, y=260)
    t3= Entry(top)
    t3.place(x=270, y=260)

    def calculate():
        try:
            global amount
            amount= int(value.get())

            note2000= amount // 2000
            amount= amount% 2000
            note500= amount//500
            amount= amount%500
            note100= amount // 100
            amount= amount%100

            t1.delete(0,END)
            t2.delete(0, END)
            t3.delete(0,END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error","Please enter valid number." )
    calc_btn= Button(top, text="Calculate", command=calculate)
    calc_btn.place(x=250, y=120)
    top.mainloop()

def new():
    msg= messagebox.showinfo("Alert!", "do you want to calculate the denomination count?")
    if msg=="ok":
        topwin()

intro_btn= Button(text="Let's Get Started", fg="white", bg="red", command= new)
intro_btn.place(x=260, y=360)

window.mainloop()

