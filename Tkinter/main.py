from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)


def button_clicked():
    print("Button clicked")


# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New Button
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=2, row=2)

window.mainloop()
