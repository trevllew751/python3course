from random import shuffle
from Demo.card import Card


class Deck:

    def __init__(self):
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num_cards):
        deck_size = self.count()
        if deck_size == 0:
            raise ValueError("All cards have been dealt")
        num_remove = min(num_cards, deck_size)
        cards = self.cards[-num_remove:]
        self.cards = self.cards[:-num_remove]
        return cards

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num_cards):
        return self._deal(num_cards)
