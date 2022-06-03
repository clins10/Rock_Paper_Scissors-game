import random
from xml.etree.ElementTree import Comment

keep_running = True
list_of_options = ['R', 'P', 'S'] #list of options
options_explanation = {
    'R' : 'Rock',
    'P' : 'Paper',
    'S' : 'Scissors'
}

def play_game():
    global keep_running
    print("Welcome 👋👋... to Rock 👊, Paper 📰 And Scissors ✂️  game! @CollinsViashima")
    print("Game Rules ✍️: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
    print("Have fun 💤💤 !")
    user = input("pick an option 'R' or 'P' or 'S': ")
    user = user.lower() #converting user input to lowercase
    user = user.strip() #removing whitespace
    user = user.upper() #converting user input to uppercase
    
    computer = random.choice(list_of_options) #randomly choosing an option from the list

    if user in list_of_options:
        if user == computer:
            return (f"You picked ({options_explanation[user]}) And The Computer also picked ({options_explanation[computer]}) so, It's a tie 🤝🤝!\n pick an option to play again!")

        if is_win(user, computer):
            keep_running = False
            return (f"You picked ({options_explanation[user]}) And The Computer picked ({options_explanation[computer]}) Congrats...  You Win 🎉🎉!")

        keep_running = False
        return (f"You picked ({options_explanation[user]}) And The Computer picked ({options_explanation[computer]}) sorry... You Lose 😭😭 !")
    else:
        return ("Invalid Input 🛑 !  please pick 'R' or 'P' or 'S'")


def is_win(player, opponent):
    if player == 'R' and opponent == 'S':
        return True 
    elif player == 'S' and opponent == 'P':
        return True 
    
    elif player == 'P' and opponent == 'R': 
        return True
    else:
        return False 

#while loop to keep the game running
while keep_running:
    print(play_game()) #calling the play_game function

Comment= 'link up me on LinkedIn: https://www.linkedin.com/in/collins-viashima-b8a9b9a1/'
