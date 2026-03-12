import unittest
from main import update_game_state 


class TestUpdateGameState(unittest.TestCase):

    def test_duplicate_guess(self):
        letters, lives, status = update_game_state("apple", ["a"], "a", 6)
        self.assertEqual(status, "Duplicate")
        self.assertEqual(lives, 6)

    def test_invalid_guess(self):
        letters, lives, status = update_game_state("apple", [], "1", 6)
        self.assertEqual(status, "Invalid")
        self.assertEqual(lives, 6)

    def test_correct_guess(self):
        letters, lives, status = update_game_state("apple", [], "a", 6)
        self.assertEqual(status, "Correct")
        self.assertIn("a", letters)

    def test_wrong_guess(self):
        letters, lives, status = update_game_state("apple", [], "z", 6)
        self.assertEqual(status, "Wrong")
        self.assertEqual(lives, 5)

    def test_victory_by_word(self):
        letters, lives, status = update_game_state("apple", [], "apple", 6)
        self.assertEqual(status, "Victory")


if __name__ == "__main__":
    unittest.main()