from tkinter import *

window = Tk()
window.title("Mile To Kilometer Converter")
window.config(padx=20, pady=20)

def convert():
    mile = float(input.get())
    kilo = mile * 1.60934
    kilometer.config(text=f"{kilo}")

input = Entry(width=7)
input.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

kilometer = Label(text="0")
kilometer.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

calculate = Button(text="Convert", command=convert)
calculate.grid(column=1, row=2)

window.mainloop()