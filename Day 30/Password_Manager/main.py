from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
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
    new_data = {
        get_website: {
            "email": get_username,
            "password": get_password,
        }
    }

    if len(get_website) == 0 or len(get_password) == 0:
        messagebox.showinfo(title="Oops", message="Please fill out all the fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_text.delete(0, END)
            password_text.delete(0, END)

        #FIND PASSWORD

def find_password():
    website = website_text.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} found.")

        #UI SETUP

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Logo
canvas = Canvas(height=180, width=180, highlightthickness=0)
logo = PhotoImage(file="Logo.png")
canvas.create_image(90, 90, image=logo)
canvas.grid(row=0, column=1, pady=(0, 20))

# Labels
Label(text="Website:").grid(row=1, column=0, sticky="e")
Label(text="Email/Username:").grid(row=2, column=0, sticky="e")
Label(text="Password:").grid(row=3, column=0, sticky="e")

# Entries
website_text = Entry(width=21)
website_text.grid(row=1, column=1, sticky="w")
website_text.focus()

username_text = Entry(width=35)
username_text.grid(row=2, column=1, columnspan=2, sticky="w")
username_text.insert(0, "example@gmail.com")

password_text = Entry(width=21)
password_text.grid(row=3, column=1, sticky="w")

# Buttons
search = Button(text="Search", width=13, command=find_password)
search.grid(row=1, column=2, padx=(5, 0))

generate = Button(text="Generate Password", width=13, command=generate_password)
generate.grid(row=3, column=2, padx=(5, 0))

add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2, pady=(10, 0))

window.mainloop()