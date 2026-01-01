#p means principal amount, r means rate of interest, t means time, simple interest formula- ptr/100

from tkinter import *

window = Tk()
window.title("Interest Calculator")
window.geometry("400x350")

def calculate():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())


    simple_interest = (p * r * t) / 100
    compound_interest = p * ((1 + r / 100) ** t) - p

    si_label.config(text=f"Simple Interest: {simple_interest:.2f}")
    ci_label.config(text=f"Compound Interest: {compound_interest:.2f}")

pa_label= Label(window, text="Principal Amount")
pa_label.pack()
principal_entry = Entry(window)
principal_entry.pack()

rate_o_i= Label(window, text="Rate of Interest (%)")
rate_o_i.pack()
rate_entry = Entry(window)
rate_entry.pack()

time_period= Label(window, text="Time Period (years)")
time_period.pack()
time_entry = Entry(window)
time_entry.pack()

calc_btn= Button(window, text="Calculate", command=calculate)
calc_btn.pack(pady=10)

si_label = Label(window, text="") 
si_label.pack()

ci_label = Label(window, text="")
ci_label.pack()

window.mainloop()