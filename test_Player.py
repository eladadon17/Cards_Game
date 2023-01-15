from unittest import TestCase
from Player import Player

class TestPlayer(TestCase):

    def setUp(self):
        self.elad=Player('elad',15)


    def test__init__valid_case_True(self):
        self.assertTrue(self.elad)
        self.assertEqual('elad',self.elad.name)
        self.assertEqual(15,self.elad.number_cards)

    def test__init__valid_case_False(self):



    def test_set_hand(self):
        self.fail()


    def test_get_card(self):
        self.fail()


    def test_add_card(self):
        self.fail()