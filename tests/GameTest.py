import unittest

from src.Game import Game


class GameTest(unittest.TestCase):
    def test_game_initializes_with_score_of_zero(self):
        game = Game()
        self.assertEqual(0, game.score())

    def test_roll_all_1_score_20(self):
        game = Game()

        i = 0
        while i < 20:
            game.roll(1)
            i += 1

        self.assertEqual(20, game.score())
