import csv, random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        suits = ["♥", "♦", "♣", "♠"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.shuffle()
    
    def shuffle(self):
         random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return None
    
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
      self.cards.append(card)
      if card.rank in ['Jack', 'Queen', 'King']:
          self.value += 10
      elif card.rank != 'Ace':
          self.value += int(card.rank)
      else:
          self.value += 11
          self.aces += 1
      while self.value > 21 and self.aces > 0:
          self.value -= 10
          self.aces -= 1
          
    def __str__(self):
        card_strings = [str(card) for card in self.cards]
        return ", ".join(card_strings) + f" (Value: {self.value})"

def play_blackjack():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    for _ in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    print("Your hand:", player_hand)
    print("Dealer's face-up card:", dealer_hand.cards[0])

    while True:
        action = input("Hit or Stand? (h/s): ").lower()
        if action == 'h':
            player_hand.add_card(deck.deal())
            print("Your hand:", player_hand)
            if player_hand.value > 21:
                print("Bust! You lose.")
                return
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    print("Dealer's hand:", dealer_hand)
    while dealer_hand.value < 17:
        dealer_hand.add_card(deck.deal())
        print("Dealer hits:", dealer_hand)
        if dealer_hand.value > 21:
          print("Dealer busts! You win!")
          return
    
    if dealer_hand.value > player_hand.value:
      print("Dealer wins!")
    elif dealer_hand.value < player_hand.value:
      print("You win!")
    else:
      print("It's a push!")
      
play_blackjack()