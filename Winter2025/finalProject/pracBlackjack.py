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
'''
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