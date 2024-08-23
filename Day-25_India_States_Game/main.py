import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States Game")

image = "D:\Raghav soni\Git Files\Python_100_Days_of_Code_Projects\Day-25_India_States_Game\India_Map.gif"
screen.addshape(image)
turtle.shape(image)

# To find coordinates of states on turtle screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

states_df = pandas.read_csv("D:\Raghav soni\Git Files\Python_100_Days_of_Code_Projects\Day-25_India_States_Game\states.csv")
all_states = states_df.state.to_list()
guest_state = []

while len(guest_state)<36:
    answer_state = screen.textinput(title=f"{len(guest_state)}/35 Guess the state", prompt="What's another state's or union territory name?").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        state_info = states_df[states_df.state == answer_state]

        write = turtle.Turtle()
        write.hideturtle()
        write.penup()
        write.goto((float(state_info.x.item()), float(state_info.y.item())))
        write.write(arg=f"{answer_state}", align="left", font=("Arial", 8, "normal"))

        guest_state.append(answer_state)

# Creating list of states to learn
learn_list = []
for state in all_states:
    if state not in guest_state:
        learn_list.append(state)

new_dict = {
    "Stares to learn": learn_list
}
df = pandas.DataFrame(new_dict)
df.to_csv("missing_stats.csv")
