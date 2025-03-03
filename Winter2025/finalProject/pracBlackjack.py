import random, csv


#--functions-------------------------------------------
'''
def card_value(card):
    if ranks in ('J','Q','K'):
        return int(10)
    elif ranks in ('2','3','4','5','6','7','8','9','10'):
        return int(ranks)
    elif ranks == 'A':
        print ("\n"+ str(card))
        num = input("Do you want this to be 1 or 11?\n>")
        while num !='1' or num !='11':
            if num == '1':
                return int(1)
            elif num == '11':
                return int(11)
            else:
                num = input("Do you want this to be 1 or 11?\n>")
'''

#--MAIN EXECUTING CODE---------------------------------


suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
suits_symbols = {"Hearts": "♥", "Diamonds": "♦", "Clubs": "♣", "Spades": "♠"}
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
values = {"2": 2, "3": 3, "4": 4, "5": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11,}

def print_deck():
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for suit in suits:
        for rank in ranks:
            print(f"{rank}{suits_symbols[suit]}", end="  ")
        print()

import random

def deal_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        if card.isdigit():
            value += int(card)
        elif card in ('J', 'Q', 'K'):
            value += 10
        elif card == 'A':
            value += 11
            ace_count += 1
    while value > 21 and ace_count > 0:
        value -= 10
        ace_count -= 1
    return value

def display_hands(player_hand, dealer_hand, hide_dealer=True):
    print("\nDealer's hand:")
    if hide_dealer:
        print("[Hidden Card]", dealer_hand[1])
    else:
        print(*dealer_hand)
    print("Value:", calculate_hand_value(dealer_hand) if not hide_dealer else "?")

    print("\nYour hand:", *player_hand)
    print("Value:", calculate_hand_value(player_hand))

def play_blackjack():
    deck = [str(i) for i in range(2, 11)] * 4 + ['J'] * 4 + ['Q'] * 4 + ['K'] * 4 + ['A'] * 4
    random.shuffle(deck)

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    while True:
        display_hands(player_hand, dealer_hand)
        player_value = calculate_hand_value(player_hand)
        if player_value == 21:
            print("\nBlackjack! You win!")
            return
        
        action = input("\nHit or Stand? (h/s): ").lower()
        if action == 'h':
            player_hand.append(deal_card(deck))
            if calculate_hand_value(player_hand) > 21:
                display_hands(player_hand, dealer_hand, hide_dealer=False)
                print("\nBust! You lose.")
                return
        elif action == 's':
             break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    display_hands(player_hand, dealer_hand, hide_dealer=False)

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21:
        print("\nDealer busts! You win!")
    elif dealer_value > player_value:
        print("\nDealer wins!")
    elif dealer_value < player_value:
        print("\nYou win!")
    else:
        print("\nIt's a push (tie).")


        
play_blackjack()
'''

import random 
  
card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] 
deck = [(card, category) for category in card_categories for card in cards_list] 
  
def card_value(card): 
    if card[0] in ['Jack', 'Queen', 'King']: 
        return 10
    elif card[0] == 'Ace': 
        return 11
    else: 
        return int(card[0]) 
  
random.shuffle(deck) 
player_card = [deck.pop(), deck.pop()] 
dealer_card = [deck.pop(), deck.pop()] 
  
while True: 
    player_score = sum(card_value(card) for card in player_card) 
    dealer_score = sum(card_value(card) for card in dealer_card) 
    print("Cards Player Has:", player_card) 
    print("Score Of The Player:", player_score) 
    print("\n") 
    choice = input('What do you want? ["play" to request another card, "stop" to stop]: ').lower() 
    if choice == "play": 
        new_card = deck.pop() 
        player_card.append(new_card) 
    elif choice == "stop": 
        break
    else: 
        print("Invalid choice. Please try again.") 
        continue
  
    if player_score > 21: 
        print("Cards Dealer Has:", dealer_card) 
        print("Score Of The Dealer:", dealer_score) 
        print("Cards Player Has:", player_card) 
        print("Score Of The Player:", player_score) 
        print("Dealer wins (Player Loss Because Player Score is exceeding 21)") 
        break
  
while dealer_score < 17: 
    new_card = deck.pop() 
    dealer_card.append(new_card) 
    dealer_score += card_value(new_card) 
  
print("Cards Dealer Has:", dealer_card) 
print("Score Of The Dealer:", dealer_score) 
print("\n") 
  
if dealer_score > 21: 
    print("Cards Dealer Has:", dealer_card) 
    print("Score Of The Dealer:", dealer_score) 
    print("Cards Player Has:", player_card) 
    print("Score Of The Player:", player_score) 
    print("Player wins (Dealer Loss Because Dealer Score is exceeding 21)") 
elif player_score > dealer_score: 
    print("Cards Dealer Has:", dealer_card) 
    print("Score Of The Dealer:", dealer_score) 
    print("Cards Player Has:", player_card) 
    print("Score Of The Player:", player_score) 
    print("Player wins (Player Has High Score than Dealer)") 
elif dealer_score > player_score: 
    print("Cards Dealer Has:", dealer_card) 
    print("Score Of The Dealer:", dealer_score) 
    print("Cards Player Has:", player_card) 
    print("Score Of The Player:", player_score) 
    print("Dealer wins (Dealer Has High Score than Player)") 
else: 
    print("Cards Dealer Has:", dealer_card) 
    print("Score Of The Dealer:", dealer_score) 
    print("Cards Player Has:", player_card) 
    print("Score Of The Player:", player_score) 
    print("It's a tie.")
'''