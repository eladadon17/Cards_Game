from unittest import TestCase
from Card import Card

class TestCard(TestCase):
    pass
    def setUp(self):
        self.card=Card(13,1)

    def test__init__valid(self):
        self.assertTrue(self.card)
        self.assertEqual(1, self.card.suit)
        self.assertEqual(13, self.card.value)

    def test__init__invalid_value(self):
        with self.assertRaises(TypeError):
            card = Card('asd', 3)
        with self.assertRaises(ValueError):
            card=Card(0,1)
        with self.assertRaises(ValueError):
            card=Card(14,1)

    def test__init__invalid_suit(self):
        with self.assertRaises(TypeError):
            card = Card(12, 'asd')
        with self.assertRaises(ValueError):
            card=Card(10,0)
        with self.assertRaises(ValueError):
            card=Card(10,5)

    def test__gt__valid_case_true(self):
        card1=Card(13,4)
        card2=Card(1,4)
        self.assertTrue(card2>card1)
        card1=Card(10,4)
        card2=Card(10,1)
        self.assertTrue(card1>card2)
        card1=Card(10,2)
        card2=Card(5,2)
        self.assertTrue(card1>card2)

    def test__gt__valid_case_false(self):
        card1 = Card(13, 4)
        card2 = Card(1, 4)
        self.assertFalse(card2 < card1)
        card1 = Card(10, 4)
        card2 = Card(10, 1)
        self.assertFalse(card1 < card2)
        card1 = Card(10, 2)
        card2 = Card(5, 2)
        self.assertFalse(card1 < card2)

    def test__gt__invalid_case(self):
        card1 = Card(2, 4)
        card2 = (2, 4)
        with self.assertRaises(TypeError):
            (card1==card2)
            (card2>card1)