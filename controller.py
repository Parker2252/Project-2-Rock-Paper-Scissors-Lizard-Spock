from tkinter import *
import tkinter.font as font
import random

user_score = 0
computer_score = 0
possibleHands = ['rock', 'paper', 'scissors', 'lizard', 'spock']


def player_choice(player_input):
    """
    :param player_input: What button the player selects
    :return: Player_input and computer_input as well as who won the round, then gives 1 point to the winner.
    """
    global user_score, computer_score

    computer_input = get_computer_choice()

    player_choice_label.config(text='Your Selected : ' + player_input)
    computer_choice_label.config(text='Computer Selected : ' + computer_input)

    if player_input == computer_input:
        winner_label.config(text="Tie")
    elif (player_input == 'scissors' and computer_input == 'paper') or (
            player_input == 'paper' and computer_input == 'rock') or (
            player_input == 'rock' and computer_input == 'lizard' or (
            player_input == 'lizard' and computer_input == 'spock') or (
                    player_input == 'spock' and computer_input == 'scissors') or (
                    player_input == 'scissors' and computer_input == 'lizard') or (
                    player_input == 'lizard' and computer_input == 'paper') or (
                    player_input == 'paper' and computer_input == 'spock') or (
                    player_input == 'spock' and computer_input == 'rock') or (
                    player_input == 'rock' and computer_input == 'scissors')):
        user_score += 1
        winner_label.config(text="You Won!!!")
        player_score_label.config(text='Your Score : ' + str(user_score))
        if user_score == 3:
            winner_label.config(text="You have won the match!!!")
            computer_score = 0
            user_score = 0
            player_score_label.config(text='Your Score : ' + str(user_score))
            computer_score_label.config(text='Your Score : ' + str(computer_score))

    else:
        computer_score += 1
        winner_label.config(text="Computer Won!!!")
        computer_score_label.config(text='Your Score : ' + str(computer_score))
        if computer_score == 3:
            winner_label.config(text="Computer Won has won the match!!!")
            computer_score = 0
            user_score = 0
            player_score_label.config(text='Your Score : ' + str(user_score))
            computer_score_label.config(text='Your Score : ' + str(computer_score))

    user_test = Label(game_window)
    user_test.place(x=170, y=250)

    computer_label = Label(game_window)
    computer_label.place(x=600, y=250)

    # Logic to display player_input
    if player_input == 'scissors':
        user_test.config(image=image_scissors)
    if player_input == 'rock':
        user_test.config(image=image_rock)
    if player_input == 'paper':
        user_test.config(image=image_paper)
    if player_input == 'lizard':
        user_test.config(image=image_lizard)
    if player_input == 'spock':
        user_test.config(image=image_spock)

    # Logic to display computer_input
    if computer_input == 'scissors':
        computer_label.config(image=image_scissors)
    if computer_input == 'rock':
        computer_label.config(image=image_rock)
    if computer_input == 'paper':
        computer_label.config(image=image_paper)
    if computer_input == 'lizard':
        computer_label.config(image=image_lizard)
    if computer_input == 'spock':
        computer_label.config(image=image_spock)


# Function to Randomly Select Computer Choice
def get_computer_choice():
    """
    Gets choice for the computer
    :return: Computer choice
    """
    return random.choice(possibleHands)


game_window = Tk()
game_window.title("Rock Paper Scissors Lizard Spock Game")

image_rock = PhotoImage(file="Rock.PNG")
label_rock = Label(game_window, image=image_rock)
# label_rock.grid(row=7, column=7,)

image_paper = PhotoImage(file="Paper.PNG")
label_paper = Label(game_window, image=image_paper)

image_scissors = PhotoImage(file="Scissors.PNG")
label_scissors = Label(game_window, image=image_scissors)

image_lizard = PhotoImage(file="Lizard.PNG")
label_lizard = Label(game_window, image=image_lizard)

image_spock = PhotoImage(file="Spock.png")
label_spock = Label(game_window, image=image_spock)

app_font = font.Font(size=12)

# Displaying Game Title
game_title = Label(text='Rock Paper Scissors Lizard Spock Best of 3', font=font.Font(size=20), fg='Black')
game_title.pack()

# Label to display, who wins each time
winner_label = Label(text="Let's Start the Game...", fg='green', font=font.Font(size=13), pady=8)
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack()

# Displaying player options
player_options = Label(input_frame, text="Take Your Pick : ", font=app_font, fg='black')
player_options.grid(row=1, column=0, pady=8)

rock_btn = Button(input_frame, text='Rock', width=15, bd=0, bg='pink', pady=5,
                  command=lambda: player_choice(possibleHands[0]))
rock_btn.grid(row=1, column=1, padx=8, pady=5)

paper_btn = Button(input_frame, text='Paper', width=15, bd=0, bg='silver', pady=5,
                   command=lambda: player_choice(possibleHands[1]))
paper_btn.grid(row=1, column=2, padx=8, pady=5)

scissors_btn = Button(input_frame, text='Scissors', width=15, bd=0, bg='purple', pady=5,
                      command=lambda: player_choice(possibleHands[2]))
scissors_btn.grid(row=1, column=3, padx=8, pady=5)

lizard_btn = Button(input_frame, text='Lizard', width=15, bd=0, bg='green', pady=5,
                    command=lambda: player_choice(possibleHands[3]))
lizard_btn.grid(row=1, column=4, padx=8, pady=5)

spock_btn = Button(input_frame, text='Spock', width=15, bd=0, bg='light blue', pady=5,
                   command=lambda: player_choice(possibleHands[4]))
spock_btn.grid(row=1, column=5, padx=8, pady=5)

# Displaying Score and players choose
score_label = Label(input_frame, text='Score : ', font=app_font, fg='grey')
score_label.grid(row=2, column=0)

player_choice_label = Label(input_frame, text='Your Selected : ---', font=app_font)
player_choice_label.grid(row=3, column=1, pady=5)

player_score_label = Label(input_frame, text='Your Score : -', font=app_font)
player_score_label.grid(row=3, column=2, pady=5)

computer_choice_label = Label(input_frame, text='Computer Selected : ---', font=app_font, fg='black')
computer_choice_label.grid(row=4, column=1, pady=5)

computer_score_label = Label(input_frame, text='Computer Score : -', font=app_font, fg='red')
computer_score_label.grid(row=4, column=2, padx=(10, 0), pady=5)

# Displaying Your choice and Computer choice
player_pick = Label(input_frame, text='Your Choice', font=app_font, fg='black')
player_pick.grid(row=6, column=1)

computer_pick = Label(input_frame, text='Computer Choice', font=app_font, fg='black')
computer_pick.grid(row=6, column=4)

# Size of the window also nonresident
game_window.geometry('900x420')
game_window.resizable(False, False)
game_window.mainloop()
