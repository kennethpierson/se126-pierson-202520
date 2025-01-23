#Name
#W9 #Final Project
#Date December 8, 2024
#SE116.02

#For the final project in the course, you will be creating your own program prompt similar to the midterm project.  You will then design, test, and code the solution file.  This will serve as your final review for the course and help prepare you for SE126.
#Program Specifics - The program you develop must show an understanding of all major course topics: Documentation, Input/Output, Processing & Assignment, Control Flow, Both repetition and single decision statements must be included. Functions Both built-in and developer-created functions must be included'''

#VARIABLE DICTIONARY

#---IMPORTS---------------------------------------------------
from os import system, name
#---FUNCTIONS-------------------------------------------------
def clear():
    if name == "nt": #for windows
        _ = system("cls")
    else: #for mac or linux
        _ = system("clear")

def loopcontrol(): #() is empty so NO parameters; this function does not require any info to run
    ans = input("Would you like to Shoot Again? [y/n]: ").lower()
    while ans != "y" and ans != "n":
      print("***INVALID ENTRY***")
      ans = input("Would you like to Shoot Again? [y/n]: ").lower()
    return ans

#---------------------------------------------------------------------

#start code below :]

count_wins = 0
count_losses = 0
count_draw = 0

import random

# Print rules for the game
print("\n***Welcome to ROCK PAPER SCISSORS LIZARD SPOCK***\n")
print("Below are the Rules of the Game:\n")
print("Scissors Cuts Paper")
print("Paper Covers Rock")
print("Rock Crushes Lizard")
print("Lizard Poisons Spock")
print("Spock Smashes Scissors")
print("Scissors Decapitates Lizard")
print("Lizard Eats Paper")
print("Paper Disproves Spock")
print("Spock Vaporizes Rock")
print("And as it always has Rock Crushes Scissors\n")

answer = input("Ready to Shoot? [y/n]: ").lower()
print()

#invalid entry trap - user will only enter this if they do not follow the directions from prior prompt
while answer != "y" and answer != "n":
  print("***INVALID ENTRY***")
  answer = input("Ready to Shoot? [y/n]: ").lower()
while answer == "y":

    player_choice = input("Enter a choice (Rock, Paper, Scissors, Lizard, Spock): ").upper()
    game_options = ["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"]
    if player_choice not in game_options:
        print("***INVALID ENTRY***")
        continue
    computer_choice = random.choice(game_options)

    print(f"\nPlayer's Choice:   {player_choice}\nComputer's Choice: {computer_choice}\n")

    if player_choice == computer_choice:
        print(f"Both players selected {player_choice}. It's a tie!")
        count_draw += 1
    elif player_choice == "ROCK":
        if computer_choice == "SCISSORS":
            print("Rock Crushes Scissors! You Win!")
        if computer_choice == "LIZARD":
            print("Rock Crushes Lizard! You Win!")
        if computer_choice == "PAPER":
            print("Paper Covers Rock! You Lose.")
        if computer_choice == "SPOCK":
            print("Spock Vaporizes Rock! You Lose.")
        if player_choice == "ROCK" and computer_choice == "SCISSORS":
            count_wins += 1
        if player_choice == "ROCK" and computer_choice == "LIZARD":
            count_wins += 1
        if player_choice == "ROCK" and computer_choice == "PAPER":
            count_losses += 1
        if player_choice == "ROCK" and computer_choice == "SPOCK":
            count_losses += 1
    elif player_choice == "PAPER":
        if computer_choice == "ROCK":
            print("Paper Covers Rock! You Win!")
        if computer_choice == "SPOCK":
            print("Paper Disproves Spock! You Win")
        if computer_choice == "SCISSORS":
            print("Scissors Cuts Paper! You Lose.")
        if computer_choice == "LIZARD":
            print("Lizard Eats Paper! You Lose")
        if player_choice == "PAPER" and computer_choice == "ROCK":
            count_wins += 1
        if player_choice == "PAPER" and computer_choice == "SPOCK":
            count_wins += 1
        if player_choice == "PAPER" and computer_choice == "SCISSORS":
            count_losses += 1
        if player_choice == "PAPER" and computer_choice == "LIZARD":
            count_losses += 1
    elif player_choice == "SCISSORS":
        if computer_choice == "PAPER":
            print("Scissors Cuts Paper! You Win!")
        if computer_choice == "LIZARD":
            print("Scissors Decapitates Lizard! You Win!")
        if computer_choice == "ROCK":
            print("Rock Crushes Scissors! You Lose!")
        if computer_choice == "SPOCK":
            print("Spock Smashes Scissors! You Lose!")
        if player_choice == "SCISSORS" and computer_choice == "PAPER":
            count_wins += 1
        if player_choice == "SCISSORS" and computer_choice == "LIZARD":
            count_wins += 1
        if player_choice == "SCISSORS" and computer_choice == "ROCK":
            count_losses += 1
        if player_choice == "SCISSORS" and computer_choice == "SPOCK":
            count_losses += 1
    elif player_choice == "LIZARD":
        if computer_choice == "SPOCK":
            print("Lizard Poisons Spock! You Win!")
        if computer_choice == "PAPER":
            print("Lizard Eats Paper! You Win")
        if computer_choice == "SCISSORS":
            print("Scissors Decapitates Lizard! You Lose")
        if computer_choice == "ROCK":
            print("Rock Crushes Lizard! You Lose!")
        if player_choice == "LIZARD" and computer_choice == "SPOCK":
            count_wins += 1
        if player_choice == "LIZARD" and computer_choice == "PAPER":
            count_wins += 1
        if player_choice == "LIZARD" and computer_choice == "SCISSORS":
            count_losses += 1
        if player_choice == "LIZARD" and computer_choice == "ROCK":
            count_losses += 1    
    elif player_choice == "SPOCK":
        if computer_choice == "SCISSORS":
            print("Spock Smashes Scissors! You Win!")
        if computer_choice == "ROCK":
            print("Spock Vaporizes Rock! You Win!")
        if computer_choice == "LIZARD":
            print("Lizard Poisons Spock! You Lose!")
        if computer_choice == "PAPER":
            print("Paper Disproves Spock! You Lose!")
        if player_choice == "SPOCK" and computer_choice == "SCISSORS":
            count_wins += 1
        if player_choice == "SPOCK" and computer_choice == "ROCK":
            count_wins += 1
        if player_choice == "SPOCK" and computer_choice == "LIZARD":
            count_losses += 1
        if player_choice == "SPOCK" and computer_choice == "PAPER":
            count_losses += 1    
    print()
    answer = loopcontrol()
    clear()
total_games = count_wins + count_losses +  count_draw
avg_wins = (count_wins/total_games) * 100
print(f"Total Games Played: {total_games}")
print()
print(f"You had {count_wins} win(s) | {count_losses} loss(es) | {count_draw} tie(s)!\n ")
print(f"Winning Percentage is: {avg_wins:.0f}%\n ")
print("Thanks for playing! Live Long and Prosper\n")