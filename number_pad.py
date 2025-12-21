from tkinter import *

window= Tk()
window.geometry("300x400")
window.title("number pad")

frame= Frame(master=window, height=2, width= 5, bg= "#E259A4")
num= [[9,8,7],[6,5,4], [3,2,1], ["#",0,"*"]]
for i in range(4):
    window.columnconfigure(i, weight=1, minsize= 75)
    window.rowconfigure(i, weight=1, minsize= 50)

    for j in range(0,3):
        frame= Frame(master=window, relief= SUNKEN, borderwidth=1 , bg="blue")
        frame.grid(row=i, column=j)
        label= Label(master=frame, text=num[i][j], bg="#8ED0E4")
        label.pack(padx=5, pady=5)
window-mainloop()