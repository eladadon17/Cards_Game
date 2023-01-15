from Player import Player
from Deck_Of_Cards import DeckOfCards

class CardGame:

    def __init__(self, name1, name2, num_cards1=26, num_cards2=26):
        # if num_cards1 < 10 or quantity > 26:
        #     quantity=26
        self.player1=Player(name1,num_cards1)
        self.player2=Player(name2, num_cards2)
        self.deck_cards=DeckOfCards()
        self.game=self.new_game()


    def new_game(self):
        if len(self.deck_cards.cards) == 52:
            self.deck_cards.cards_shuffle()
            self.player1.set_hand(self.deck_cards)
            self.player2.set_hand(self.deck_cards)
        else:
            print("Error")

    def get_winner(self):
        if len(self.player1.cards) > len(self.player2.cards):
            return f'the winner is: {self.player1.name.title()}'
        if len(self.player1.cards) < len(self.player2.cards):
            return f'the winner is: {self.player2.name.title()}'
        if len(self.player1.cards) == len(self.player2.cards):
            return None

# asd=CardGame()
# asd.new_game(DeckOfCards())
# print(asd.player1)
# print(asd.player2)