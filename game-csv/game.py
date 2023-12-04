import pandas as pd
import turtle as t

state_df = pd.read_csv("50_states.csv")

type(state_df)


timmy = t.Turtle()
screen = t.Screen()
timmy.ht()
screen.bgpic("blank_states_img.gif")


states = 0
guessed_state = []
all_states = state_df["state"].to_list()
while len(guessed_state) < 50:
    choice = screen.textinput(f"States{states}/50", "Enter the name of the states:")
    if choice == "Exit":
        break
    elif choice in state_df["state"].values:
        state_info = state_df[state_df["state"] == choice].iloc[0]
        timmy.teleport(state_info["x"], state_info["y"])
        guessed_state.append(state_info["state"])
        timmy.write(guessed_state[states])
        states += 1
    else:
        print(f"State '{choice}' not found in the DataFrame.")

not_guessed_state = [value for value in all_states if value not in guessed_state]
not_guessed_state_df = pd.DataFrame(not_guessed_state)
not_guessed_state_df.to_csv("not_guessed_state_df.csv")