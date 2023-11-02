from tkinter import *
# For error popups
from tkinter import messagebox
# To Generate random password
from random import choice, randint, shuffle
# To copy password to the clipboard
import pyperclip
# To store data
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letter_list + symbols_list + numbers_list
    shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # variables
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # Empty fields
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:  # Open File
            with open("data.json", "r") as data_file:
                # Read old data
                data = json.load(data_file)
                # Update data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Create new data
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                # Save updated data
                json.dump(data, data_file, indent=4)

        # Clear data
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- Search Password ------------------------------- #


def search():
    website = website_entry.get()
    try:  # Read the file
        with open("data.json", "r") as data_file:
            file = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:  # Search using website entry
        if len(website) != 0:
            try:  # Search through the data_file
                found_entry = file[website.lower()]
            except KeyError:
                messagebox.showinfo(title="Error", message="No details for the website exists")
            else:
                messagebox.showinfo(title=website, message=f"Email: {found_entry['email']} \n "
                                                           f"Password: {found_entry['password']}")
        else:
            messagebox.showinfo(message="Write something in the website entry")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=20)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ebizimana@mmskids.org")
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1, padx=1)

# Button
search_button = Button(text="Search", width=11, command=search)
search_button.grid(row=1, column=2)
generate_button = Button(text="Generate Password", width=11, command=generate_password)
generate_button.grid(row=3, column=2, padx=1)
add_button = Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
