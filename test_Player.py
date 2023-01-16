from unittest import TestCase, mock
from Player import Player
from unittest.mock import patch
from Deck_Of_Cards import DeckOfCards
from Card import Card

class TestPlayer(TestCase):

    def setUp(self):
        self.elad=Player('elad',10)
        self.deck1=DeckOfCards()

    def test__init__valid_case_True(self):
        self.assertTrue(self.elad)
        self.assertEqual(10, self.elad.number_cards)
        self.assertEqual('elad',self.elad.name)

    def test__init__valid_case_True_not_filled(self):
        eli=Player('eli')
        self.assertEqual('eli', eli.name)

    def test__init__valid_case_True_high_low(self):
        eli=Player('eli',32)
        self.assertEqual(26,eli.number_cards)
        eli = Player('eli', 8)
        self.assertEqual(26, eli.number_cards)

    def test__init__invalid_case_name_not_str(self):
        with self.assertRaises(TypeError):
            avi_neelavi=Player(12)
            avi_neelavi=Player[12]

    def test__init__invalid_case__num_cards__not_int(self):
        with self.assertRaises(TypeError):
            avi_neelavi = Player('avi', 'asd')
            avi_neelavi = Player('avi', [asd])

    @mock.patch('Deck_Of_Cards.DeckOfCards.deal_one',return_value=Card(1,4))
    def test_set_hand_valid(self,mock_deal_one):
        deck1=DeckOfCards()
        eli=Player('eli', 10)
        eli.set_hand(deck1)
        self.assertIn(Card(1,4),eli.cards)
        self.assertEqual(10,len(eli.cards))
        print(eli.cards)
        deck2 = DeckOfCards()
        maryano = Player('maryano', 26)
        maryano.set_hand(deck2)
        self.assertIn(Card(1,4), maryano.cards)
        self.assertEqual(26,len(maryano.cards))
        print(maryano.cards)

    def test_set_hand_invalid_already_have_cards(self):
        eli=Player('eli',10)
        eli.set_hand(self.deck1)
        self.assertEqual(10,len(eli.cards))
        self.assertFalse(eli.set_hand(self.deck1))
        self.assertEqual(10,len(eli.cards))

    def test_set_hand_invalid_not_enough_cards_in_deck(self):
        eli=Player('eli',26)
        eli.set_hand(self.deck1)
        self.assertEqual(26,len(eli.cards))

        maryano=Player('maryano',10)
        maryano.set_hand(self.deck1)
        self.assertEqual(10,len(maryano.cards))

        elad=Player('elad',10)
        self.assertFalse(elad.set_hand(self.deck1))
        self.assertEqual(0,len(elad.cards))

    def test_get_card_valid_case_have_cards(self):
        eli=Player('eli',10)
        eli.set_hand(self.deck1)
        self.assertEqual(10, len(eli.cards))
        print(eli.cards)
        c=eli.get_card()
        print(c)
        print(eli.cards)
        self.assertEqual(9,len(eli.cards))
        self.assertNotIn(c,eli.cards)

    def test_get_card_invalid_case_have_no_cards(self):
        eli=Player('eli')
        self.assertFalse(eli.get_card())


    def test_add_card_valid_case(self):
        eli=Player('eli')
        eli.add_card(Card(1,4))
        self.assertIn(Card(1,4),eli.cards)