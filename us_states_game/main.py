from turtle import Turtle, Screen
import pandas

IMAGE = "blank_states_img.gif"

screen = Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.addshape(IMAGE)
state_data = pandas.read_csv("50_states.csv")
state_data["coordinates"] = list(zip(state_data.x, state_data.y))
state_dict = state_data.set_index("state").to_dict()["coordinates"]

img = Turtle()
img.shape(IMAGE)
writer = Turtle()
writer.ht()
writer.pu()


state_count = 0
guessed_states = set()
game_is_on = True
while state_count < 50 and game_is_on:
    answer_state = screen.textinput(title=f"Guess the state {state_count}/50", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        game_finished = False
        break
    if answer_state in state_dict and answer_state not in guessed_states:
        writer.setpos(state_dict[answer_state])
        writer.write(answer_state, align='center')
        state_count += 1
        guessed_states.add(answer_state)

if not game_finished:

    missed_states = [s for s in state_dict if s not in guessed_states]
    pandas.DataFrame(missed_states).to_csv("missed_states.csv")


screen.exitonclick()
