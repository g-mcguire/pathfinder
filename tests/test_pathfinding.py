import unittest
from collections import deque

from pathfinder.pathfinding import *
from pathfinder.generate_matrix import *

class TestPathfinding(unittest.TestCase):
    def test_small_matrix_with_path(self):
        matrix = [
            [1, 1],
            [0, 1]
        ]
        self.assertTrue(bfs(matrix))  # Path exists

    def test_no_valid_path(self):
        matrix = [
            [1, 0],
            [0, 0]
        ]
        self.assertFalse(bfs(matrix))  # No path exists

    def test_larger_matrix_with_path(self):
        matrix = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1]
        ]
        big_matrix = [
            [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
            [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
            [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1]
        ]
        self.assertTrue(bfs(matrix))  # Path exists
        self.assertTrue(bfs(big_matrix))

    def test_larger_matrix_no_path(self):
        matrix = [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1]
        ]
        self.assertFalse(bfs(matrix))  # No path exists

    def test_is_valid_move(self):
        matrix = [
            [1, 0],
            [1, 1]
        ]
        visited = set()
        self.assertTrue(is_valid_move(matrix, (1, 1), visited))  # Valid move
        visited.add((1, 1))
        self.assertFalse(is_valid_move(matrix, (1, 1), visited))  # Already visited

if __name__ == '__main__':
    unittest.main()