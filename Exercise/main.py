# day 26 exersice 3
"""
Instructions:
Take a look inside **file1.txt** and **file2.txt**. They each contain a bunch of numbers, each number on a new line.
You are going to create a list called result which contains the numbers that are common in both files
"""


def change_to_int(data):
    return [int(num) for num in data if num != ""]


with open("file1.txt", mode="r") as file1:
    with open("file2.txt", mode='r') as file2:
        data1 = file1.read().split("\n")
        data1 = change_to_int(data1)
        data2 = file2.read().split('\n')
        data2 = change_to_int(data2)
        result = [int(num) for num in data1 if num in data2]
        # print(result)

# day 26 exersice 4
"""
Instructions:
You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given 
sentence and calculates the number of letters in each word.Try Googling to find out how to convert a 
sentence into a list of words.
Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
"""


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {item: len(item) for item in sentence.split(" ")}
# print(result)

# day 26 exersice 5
"""
Instructions:
You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature 
in degrees Celsius and converts it into degrees Fahrenheit. To convert temp_c into temp_f:
(temp_c * 9/5) + 32 = temp_f
Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
"""

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {item_key: (item_value * 9/5) + 32 for item_key, item_value in weather_c.items()}
# print(weather_f)

# day 27 Tkinter: Playground
from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# 1st method to make a label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

# Other methods to make a label
my_label["text"] = "New Text"
my_label.config(text="This is a new text")

# Button
def button_clicked():
    # my_label.config(text=input.get())
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
