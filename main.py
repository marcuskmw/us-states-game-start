import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. Status Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
df = pandas.read_csv("50_states.csv")
key_pool = df.state.to_list()
t = turtle.Turtle()
t.hideturtle()
t.penup()


def write_record_to_screen(data_record, name_of_state):
    t.goto(int(data_record.x), int(data_record.y))
    t.write(name_of_state)


finish_game = False
no_of_round = 0
total_round = len(key_pool)
while not finish_game:
    answer_state = screen.textinput(title=f"{no_of_round}/{total_round} Status Correct", prompt="Type it!")

    if answer_state:
        answer_state = answer_state.title().strip()
        if answer_state in key_pool:
            record_df = df[df.state == answer_state]
            key_pool.remove(answer_state)
            no_of_round += 1
            write_record_to_screen(record_df, answer_state)
    else:
        finish_game = True

screen.exitonclick()
