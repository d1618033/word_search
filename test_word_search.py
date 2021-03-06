import word_search
import unittest

class TestLettersInDir(unittest.TestCase):
    def setUp(self):
        self.board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def assertAllCells(self, expected_func, n):
        for i in range(3):
            for j in range(3):
                for direction in word_search.DIRECTIONS:
                    expected = expected_func(self.board[i][j])
                    actual = word_search.letters_in_dir(self.board, i, j, n, direction)
                    self.assertEqual(actual, expected)

    def test_up_2_in_middle(self):
        i , j = 1, 2
        n = 2
        direction = "up"
        expected = [5, 2]
        actual = word_search.letters_in_dir(self.board, i, j, n, direction)
        self.assertEqual(actual, expected)

    def test_n_1_always_returns_number(self):
        self.assertAllCells(lambda cell: [cell], n=1)

    def test_up_2_at_top(self):
        i , j = 0, 1
        n = 2
        direction = "up"
        expected = None
        actual = word_search.letters_in_dir(self.board, i, j, n, direction)
        self.assertEqual(actual, expected)

    def test_n_greater_than_board_always_out_of_bounds(self):
        self.assertAllCells(lambda cell: None, n=4)

    def test_down_3_at_top(self):
        i , j = 0, 0
        n = 3
        direction = "down"
        expected = [0, 3, 6]
        actual = word_search.letters_in_dir(self.board, i, j, n, direction)
        self.assertEqual(actual, expected)
