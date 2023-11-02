from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def converter():
    km = float(mile_input.get()) * 1.609344
    km = int(round(km, 0))
    number_label.config(text=km)


# Entry
mile_input = Entry(width=7)
print()
mile_input.grid(column=1, row=0)

# Mile label
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

# equal to label
equal_to_label = Label(text="Is equal to")
equal_to_label.grid(column=0, row=1)

# number label
number_label = Label(text="0")
number_label.grid(column=1, row=1)

# Km label
km_label = Label(text="km")
km_label.grid(column=2, row=1)

# Convert Button
convert = Button(text="convert", command=converter)
convert.grid(column=1, row=3)

window.mainloop()
