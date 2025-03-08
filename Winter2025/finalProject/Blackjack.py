#Tyler Phillips and Ken Pierson
#SE126.04
#Backjack
#2-26-2025

#PROMPT: 

#VARIABLE DICTIONARY:
#csvfile            Storing the relative path from the CSV file
#file               Passing the CSV file to the reader method
#rec                Processing all records in the CSV file
#i                  Index of each field of data from all records
#deck               Populated 2D list containing all the cards from the CSV file including rank and suit
#ace_count          Counts to see if there is an ace in the hand passed to the hand_value() function
#hand               Hand or 2 cards passed to hand_value() function depending on dealer or player
#total              Counts total value of hand passed to hand_value() function depending
#card               1 card containing rank and suit which is passed to hand_value() and prioritizing rank for calculation
#player_hand        Caclulated hand value of player including suit
#dealer_hand        Caclulated hand value of dealer including suit
#show_all_dealer    If this variable is labled true then the user is able to see the dealers card after playing out their hand
#ans                If this variable = "y" the program will re run [input]
#choice             If this variable = "y" the player will "hit" if "n" then the play will stand and continue the program
#player_choice      Asks player if they would like to hit or stand [input]
#dealer_value       Calucates value of dealer hand against player hand to see who won
#player_value       Calucates value of player hand against dealer hand to see who won

#-Imports-------------------------------------------------------------------------------------
#Import os for clear() function
from os import name, system
#import the CSV (comma separated value) library
import csv
#Import Random library for chosen card
import random
#-Functions-----------------------------------------------------------------------------------
def loopcontrol(): #() is empty so NO parameters; this function does not require any info to run
  ans = input("\nWould you like to play another hand? [y/n]: ").lower()
  #check the ans value, repeat back to user if necessary
  while ans != "y" and ans != "n":
    print("***INVALID ENTRY***")
    ans = input("Would you like to play another hand? [y/n]: ").lower()
  #return the ans value tp be used in the base program!
  return ans

def clear():
    if name == 'nt':        #windows os
        _ = system('cls')
    else:                   #linux or mac
        _ = system('clear')

def shuffle():      
    #Shuffles deck of cards for random hand for player and dealer
    random.shuffle(deck)

def deal(deck):     
    #Pulls last card and removes it from the list 'deck'
    return deck.pop()

def hand_value(hand):
    #Calculate hand values
    ace_count = hand.count('A')
    total = 0
    for card in hand:
        if card[1].isdigit():
            total += int(card[1])
        elif card[1] in ('J', 'Q', 'K'):
            total += 10
        elif card[1] == 'A':
            total += 11
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

def display_hands(player_hand, dealer_hand, show_all_dealer=False):
    #Displays hands and if the hand is played out the dealer will show their second card
    print(f"\n    {player_name}'s hand: {player_hand}\t\tValue: {hand_value(player_hand)}")
    if show_all_dealer:
        print(f"Dealer's hand: {dealer_hand}\t\tValue: {hand_value(dealer_hand)}")
    else:
        print(f"Dealer's hand: [{dealer_hand[0]}, {['?', '?']}]")


#-Main Code-----------------------------------------------------------------------------------

clear()     #Clear Terminal

#Empty lists
deck = []
cards = []
player = []
dealer = []

#counting variables
player_wins = 0
player_losses = 0
dealer_wins = 0
dealer_losses = 0
player_push = 0
dealer_push = 0

#--connected to file------------------------------------------
with open("text_files/cards.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        if rec[0] == "Hearts":
            rec[0] = "♥"
        elif rec[0] == "Diamonds":
            rec[0] = "♦"
        elif rec[0] == "Spades":
            rec[0] = "♠"
        elif rec[0] == "Clubs":
            rec[0] = "♣"
        
        for i in range(6):
            deck.append(rec)
#--disconnected from file---------------------------------------

#shuffle deck
shuffle()

player_name = input("Please Enter your name: ")

answer = "y"

while answer == "y":
    
    player_hand = []
    dealer_hand = []

    for i in range(2):
        player_hand.append(deal(deck))
        dealer_hand.append(deal(deck))

    choice = "y"

    while choice == "y":
        display_hands(player_hand, dealer_hand)
        player_choice = input("Hit or Stand? [h/s]: ").lower()

        if player_choice == 'h':
            player_hand.append(deal(deck))
            if hand_value(player_hand) > 21:
                choice = "n"
        elif player_choice == 's':
            while hand_value(dealer_hand) < 17:
                dealer_hand.append(deal(deck))
            choice = "n"
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    display_hands(player_hand, dealer_hand, show_all_dealer=True)

    player_value = hand_value(player_hand)
    dealer_value = hand_value(dealer_hand)

    if dealer_value > 21:
        player_wins += 1
        dealer_losses += 1
        print("Dealer busts! You win!")
    elif player_value > 21:
        dealer_wins += 1
        player_losses += 1
        print("You busted! Dealer wins.")
    elif player_value > dealer_value and player_value <= 21:
        player_wins += 1
        dealer_losses += 1
        print("You win!")
    elif dealer_value > player_value and dealer_value <= 21:
        dealer_wins += 1
        player_losses += 1
        print("Dealer win!")
    elif dealer_value == player_value:
        player_push += 1
        dealer_push += 1
        print("Neither you or the dealer won. Push.")
    else:
        print()
    
    answer = loopcontrol()

total_hands = player_wins + player_losses + player_push
player_avg = (player_wins/total_hands) * 100
dealer_avg = (dealer_wins/total_hands) * 100
print(f"\nTotal Games Played: {total_hands}\n")
print(f"{player_name} had {player_wins} win(s) | {player_losses} loss(es) | {player_push} tie(s)! ")
print(f"Winning Percentage is: {player_avg:.0f}%\n ")
print(f"Dealer had {dealer_wins} win(s) | {dealer_losses} loss(es) | {dealer_push} tie(s)! ")
print(f"Winning Percentage is: {dealer_avg:.0f}%\n ")
print("Thanks for playing! And may the Odds Ever be in Your Favor!\n")