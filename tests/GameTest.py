import unittest

from src import Game


class GameTest(unittest.TestCase):
    def test_game_initializes_with_score_of_zero(self):
        game = Game
        self.assertEqual(0, game.score())
