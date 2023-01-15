from random import choice
from Deck_Of_Cards import DeckOfCards
from Card import Card


class Player:

    def __init__(self, name, num_cards=26):
        self.name=name
        self.number_cards=num_cards
        self.cards = []

    def __repr__(self):
        return f'The deck is: {self.cards}'

    def set_hand(self, deck_cards:DeckOfCards):
        for i in range(self.number_cards):
            self.cards.append(deck_cards.deal_one())

    def get_card(self):
        # return self.cards.pop(randint(0, len(self.cards) - 1))
        c = choice(self.cards)
        self.cards.remove(c)
        return c

    def add_card(self,card):
        if type(card)!=Card:
            raise TypeError('Can add only a card')
        self.cards.append(card)



# d=DeckOfCards()
# hand1=Player('Elad',5)
# print(hand1)
# print(hand1.set_hand(d.cards))
# print(hand1.cards)
# print(hand1.get_card())
# print(hand1.cards)
# print(hand1.add_card)
# print(hand1.cards)