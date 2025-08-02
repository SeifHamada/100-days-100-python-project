from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
        #PASSWORD GENERATOR

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_text.insert(0, password)
    pyperclip.copy(password)

        #SAVE PASSWORD
def save():
    get_website = website_text.get()
    get_username = username_text.get()
    get_password = password_text.get()

    if len(get_website) == 0 or len(get_password) == 0:
        messagebox.showinfo(title="Oops", message="Please fill out all the fields.")

    else:
        is_ok = messagebox.askokcancel(title=get_website, message=f"These are the details entered: \nEmail: {get_username} "f"\nPassword: {get_password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{get_website} | {get_username} | {get_password}\n")
                website_text.delete(0, END)
                password_text.delete(0, END)

        #UI SETUP
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas= Canvas(height=200, width=200)
logo= PhotoImage(file="Logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

        #labels
website = Label(text="Website:")
website.grid(column=0, row=1)

username = Label(text="Email/Username:")
username.grid(column=0, row=2)

password= Label(text="Password:")
password.grid(column=0, row=3)

        #buttons
add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)

        #entries
website_text = Entry(width=35)
website_text.grid(row=1, column=1, columnspan=2)
website_text.focus()

username_text = Entry(width=35)
username_text.grid(row=2, column=1, columnspan=2)
username_text.insert(0, "example@gmail.com")

password_text = Entry(width=21)
password_text.grid(row=3, column=1)

window.mainloop()