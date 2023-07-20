#Lets refactor the game

import random as rnd;
rps=(0,"Rock", "Paper", "Scissors")


def choose_option():
    user_option= input("Enter your option: \n 1. Rock \n 2. Paper \n 3. Scissors \n")
    user_option= int(user_option)
    computer_option=rnd.randint(1,3)
    if not (user_option == 1 or user_option == 2 or user_option == 3 ):
        print("Invalid option")
        return choose_option()
    return user_option, computer_option

def check_rules(user_option, computer_option, win_user, win_pc):
    
        if user_option == computer_option:
            print("TIE")
            print("Computer option: ", rps[computer_option])
            print("User option: ", rps[user_option])
        elif user_option == 1 and computer_option == 2 or user_option==2 and computer_option==3 or user_option==3 and computer_option==1:
            print("You lose")
            print("Computer option: ", rps[computer_option])
            print("User option: ", rps[user_option])
            win_pc+=1
        else:
            
            print("You win")
            print("Computer option: ", rps[computer_option])
            print("User option: ", rps[user_option])
            win_user+=1
        print("Score: \n Jugador: ", win_user, "PC: ", win_pc, "\n")
        return win_pc, win_user

def check_winner(win_user, win_pc):
    if win_pc==3:
        print("""********************
    You lose the game
    ********************""")
    else:
        print("""********************
    You win the game
    ********************""")
    print("Rock, Paper, Scissors \n Jugador: ", win_user, "PC: ", win_pc, "\n")

def run_game():
    win_pc=0
    win_user=0
    while win_pc<3 and win_user<3:
        
        user_option, computer_option=choose_option()
        win_user,win_pc=check_rules(user_option, computer_option, win_user, win_pc)
    check_winner(win_user, win_pc)
    

if __name__ == "__main__":
    run_game()