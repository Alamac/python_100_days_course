from tkinter import Canvas, Button, Label, Tk, PhotoImage, Entry, END, messagebox
from pass_gen import generate_password
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def process_password():
    password = generate_password()
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.askokcancel(title="Oops",
                               message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        website_entry.delete(0, END)
        pass_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- Search password ------------------------------- #
def search_pass(website):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(message="No data file found!")
        return
    try:
        website_data = data[website]
    except KeyError:
        messagebox.showwarning(title=website, message=f"No password found for {website}")
    else:
        messagebox.showinfo(title=website,
                            message=f"Email: {website_data['email']}\nPassword: {website_data['password']}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title = "Password Manager"
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=25)
website_entry.focus()
website_entry.grid(row=1, column=1, padx=(50, 0))

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.insert(0, "alamacus@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1, padx=(24, 0))

generate_button = Button(text="Generate Password", command=process_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=lambda: search_pass(website_entry.get()))
search_button.grid(row=1, column=2)

window.mainloop()
