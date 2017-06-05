import unittest
from bowling import bowling


class GameTests(unittest.TestCase):
    def test_get_score__no_pins_knocked__returns_zero(self):
        # Arrange
        game = bowling.Game()


        # Act
        result = game.get_score()

        # Assert
        self.assertEqual(0, result)

    def test_get_score__one_pin_knocked__returns_one(self):
        # Arrange
        game = bowling.Game()
        game.record_roll(num_pins_knocked=1)

        # Act
        result = game.get_score()

        # Assert
        self.assertEqual(1, result)
