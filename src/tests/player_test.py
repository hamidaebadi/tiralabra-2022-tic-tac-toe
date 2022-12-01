import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.test_player = Player("test", 'x')
    
    def test_name_getter(self):
        self.assertEqual(self.test_player.name, "test")

    def test_sign_getter(self):
        self.assertEqual(self.test_player.sign, 'x')

    def test_turn_swap_works(self):
        #player moves
        #swap turn
        self.test_player.swap_turn()
        self.assertEqual(self.test_player.turn, False)

    def test_add_uniue_win_row(self):
        row = [(0,0), (1,1), (2,2)]
        result = self.test_player.add_win_row(row)
        self.assertEqual(result, True)

    def test_add_duplicate_win_row_fail(self):
        r1 = [(0,0),(1,1),(2,2)]
        self.test_player.add_win_row(r1)
        result = self.test_player.add_win_row(r1)
        self.assertEqual(result, False)