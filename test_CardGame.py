from unittest import TestCase
from CardGame import CardGame
from Player import Player

class TestCardGame(TestCase):

    def setUp(self):
        self.game1=CardGame('eli', 'elad',9, 9)
        self.player1 = Player('elad', 10)
        self.player2 = Player('eli', 26)
        self.player3 = Player('cheater', 8)

    def test__init_valid_case_True(self):
        self.assertTrue(self.game1)
        self.assertEqual('elad',self.player1.name)
        self.assertEqual(10,self.player1.number_cards)
        self.assertEqual([], self.player1.cards)
        self.assertEqual('eli',self.player2.name)
        self.assertEqual(26, self.player2.number_cards)
        self.assertEqual([], self.player2.cards)
        self.assertEqual('cheater',self.player3.name)
        self.assertEqual(26,self.player3.number_cards)
        self.assertEqual([],self.player3.cards)


    def test__init_valid_case_False(self):
        self.assertFalse()


    # def test__init_invalid_case(self):




    def test_new_game(self):
        self.fail()

    def test_get_winner(self):
        self.fail()
