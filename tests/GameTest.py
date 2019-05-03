import unittest

from src.Game import Game


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_roll_gutter_game(self):
        self.__roll_multiple_times(0, 20)
        self.assertEqual(0, self.game.score())

    def test_roll_all_1_score_20(self):
        self.__roll_multiple_times(1, 20)
        self.assertEqual(20, self.game.score())

    def test_roll_perfect_game_300(self):
        self.__roll_multiple_times(10, 12)
        self.assertEqual(300, self.game.score())

    def test_roll_1_strike(self):
        self.game.roll(10)
        self.game.roll(1)
        self.game.roll(1)
        self.__roll_multiple_times(0, 17)
        self.assertEqual(14, self.game.score())

    def test_roll_1_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(10)
        self.__roll_multiple_times(0, 17)
        self.assertEqual(30, self.game.score())

    def __roll_multiple_times(self, pins, rolls):
        i = 0
        while i < rolls:
            self.game.roll(pins)
            i += 1
