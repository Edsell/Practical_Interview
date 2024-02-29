 import random

# Card Class
class Card:
    def _init_(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def _repr_(self):
        return f"{self.rank} of {self.suit}"

# Deck Class
class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def _init_(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None

def cards_left(self):
        return len(self.cards)

# Hand Class
class Hand:
    def _init_(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    # Placeholder for a method that calculates the hand's value
    def get_value(self):
        pass

    def _repr_(self):
        return ', '.join(map(str, self.cards))