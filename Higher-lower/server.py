from flask import Flask
import random

app = Flask(__name__)
random_num = random.randint(0, 9)

@app.route("/")
def home_page():
    return "<h1> Guess a number between 0 and 9 </h1> " \
           "<img src='https://media2.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif?cid=ecf05e471y7apgdywioyaswptk4k9" \
           "4e6sq1tuml1psnwdxzz&rid=giphy.gif&ct=g'> "


@app.route("/<number>")
def result(number):
    if number == "3":
        return "<h1> Too Low, try again!</h1>" \
               "<img src='https://media2.giphy.com/media/jD4DwBtqPXRXa/giphy.gif?cid=790b7611796a6163ae5193620017f" \
               "8860c7dc127b60f5a89&rid=giphy.gif&ct=g'>"
    elif number == "7":
        return '<h1> Too high, try again! </h1> ' \
               '<img src="https://media4.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif?cid=790b7611f279cae1dc2b118ce3a' \
               '01434a795a63a315e5248&rid=giphy.gif&ct=g">'
    elif number == "5":
        return "<h1> You found me </h1>" \
               "<img src='https://media3.giphy.com/media/4T7e4DmcrP9du/giphy.gif?cid=790b7611d64b1ab3c8184d0fa364a4c6" \
               "8931a5bafd551392&rid=giphy.gif&ct=g'>"
    else:
        return "<h1> Please guess again</h1>"


if __name__ == "__main__":
    app.run(debug=True)
