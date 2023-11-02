import turtle
import pandas

name = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=730, height=500)

correct_answer = 0
correct_states = []

# Use a loop to allow the user to keep guessing
while correct_answer < 50:
    # Convert the guess to Title case
    answer_state = screen.textinput(title=f"{correct_answer}/50 Guess the State",
                                    prompt="What's another state's name?").title()

    # Check if the guess is among the 50 states
    file = pandas.read_csv("50_states.csv")
    check_answer = file[file["state"] == answer_state]

    # Exit the game
    if answer_state == "Exit":
        all_states = file["state"].to_list()
        wrong_states = [state for state in all_states if state not in correct_states]
        data = pandas.DataFrame(wrong_states)
        data.to_csv("states_to_learn.csv")
        break

    # Write correct guesses onto the map
    if len(check_answer) > 0 and check_answer.state.item() not in correct_states:
        x = check_answer.x.item()
        y = check_answer.y.item()
        name.up()
        name.ht()
        name.goto(x, y)
        name.write(check_answer.state.item(), align="center", font=("Courier", 10, "normal"))
        # Record the correct guesses in a list
        correct_states.append(check_answer.state.item())
        # Keep track of the score
        correct_answer += 1


screen.exitonclick()
