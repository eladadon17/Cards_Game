from Card import Card
import random
from random import choice

class DeckOfCards:

    def __init__(self):
        self.cards = []
        for suit in range(1, 5):
            for value in range(1, 14):
                self.cards.append((Card(value,suit)))


    def __repr__(self):
        return f'The deck is: {self.cards}'


    def cards_shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        # return self.deck.pop(randint(0, len(self.deck)-1))
        c = choice(self.cards)
        self.cards.remove(c)
        return c

# deck1=DeckOfCards()
# print(deck1.cards)
# print(len(deck1.cards))
# print(deck1.deal_one())
# print(len(deck1.cards))