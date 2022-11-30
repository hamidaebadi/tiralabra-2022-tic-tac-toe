import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.test_player = Player("test", 'x')
    
    def test_name_getter(self):
        self.assertEqual(self.test_player.name, "test")

    