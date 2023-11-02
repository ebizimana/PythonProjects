from tkinter import *
import pandas
from random import choice

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Read the file
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------- NEXT CARD ------------------------------- #


# Go to the next card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, flash)

# ---------------------------- SAVE PROGRESS ------------------------------- #


def is_known():
    # Move the words in a new file
    to_learn.remove(current_card)
    learn_words = pandas.DataFrame(to_learn)
    learn_words.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- FLIPPING CARD ------------------------------- #


def flash():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flash)

# Canvas
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)

# Text
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")

# Config the canvas
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR,
                      highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightbackground=BACKGROUND_COLOR,
                        highlightthickness=0, command=is_known)
correct_button.grid(row=1, column=1)

next_card()

window.mainloop()
