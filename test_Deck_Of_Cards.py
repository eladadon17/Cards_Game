from unittest import TestCase
from Deck_Of_Cards import DeckOfCards


class TestDeckOfCards(TestCase):

    def setUp(self):
        self.card1=DeckOfCards()

    def test__init__valid_case_true(self):
        self.assertTrue(self.card1.cards)
        self.assertEqual(52,len(self.card1.cards))
        print(self.card1.cards)

    def test_cards_shuffle(self):
        self.assertEqual(self.card1.cards,self.card1.cards[0::])
        self.assertNotEqual(self.card1.cards_shuffle(),self.card1.cards[0::])

    def test_deal_one_valid_case(self):
        self.assertEqual(len(self.card1.cards), 52)
        c=self.card1.deal_one()
        self.assertNotIn(c,self.card1.cards)

    def test_deal_one_invalid_case(self):
        self.card1.cards=[]
        self.assertFalse(self.card1.deal_one())
        print(self.card1.cards)