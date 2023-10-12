import unittest

from dgraph import DGraph
from search import astar, bfs, dfs, ids
from tilegameproblem import TileGame


class IOTest(unittest.TestCase):
    """
    Tests IO for search implementations. Contains basic/trivial test cases.

    Each test function instantiates a search problem (TileGame) and tests if the three test case
    contains the solution, the start state is in the solution, the end state is in the
    solution and, if applicable, if the length of the solutions are the same.

    These tests are not exhaustive and do not check if your implementation follows the
    algorithm correctly. We encourage you to create your own tests as necessary.
    """

    def _check_tilegame(self, algorithm, start_state, goal_state, length=None):
        """
        Test algorithm on a TileGame
        algorithm: algorithm to test
        start_state: start state of the TileGame
        goal_state: goal state of the TileGame
        length: length that the path returned from algorithm should be. 
                Think about why this argument is optional, and when you should provide it.
        """

        self.assertEqual(len(start_state), len(start_state[0]), "Dimensions must by n x n")
        dim = len(start_state)

        tg = TileGame(dim, start_state, goal_state)
        path = algorithm(tg)
        self.assertEqual(path[0], start_state, "Path should start with the start state")
        self.assertEqual(path[-1], goal_state, "Path should end with the goal state")
        if length:
            self.assertEqual(len(path), length, f"Path length should be {length}")

    def _check_dgraph(self, algorithm, dg, start_state, goal_state, length=None):
        """
        Check algorithm on a DGraph
        algorithm: algorithm to test
        dg: DGraph to test algorithm on
        length: length that the path returned from algorithm should be
        """
        path = algorithm(dg)
        self.assertEqual(path[0], start_state, "Path should start with the start state")
        self.assertEqual(path[-1], goal_state, "Path should end with the goal state")
        if length:
            self.assertEqual(len(path), length, f"Path length should be {length}")

    def test_bfs(self):
        self._check_tilegame(bfs, ((1, 2, 3), (4, 5, 6), (7, 8, 9)), ((1, 2, 3), (4, 5, 6), (7, 8, 9)), 1)
        self._check_tilegame(bfs, ((1, 2), (4, 3)), ((1, 2), (3, 4)), 2)
        self._check_dgraph(bfs, DGraph([[None, 1], [1, None]], {1}), 0, 1, 2)
        self._check_dgraph(bfs, DGraph([[None, 1, 3], [1, None, 1], [1, 1, None]], {2}), 0, 2, 2)
        # TODO: add tests here!

    def test_dfs(self):
        self._check_tilegame(dfs, ((1, 2, 3), (4, 5, 6), (7, 8, 9)), ((1, 2, 3), (4, 5, 6), (7, 8, 9)), 1)
        self._check_tilegame(dfs, ((1, 2), (4, 3)), ((1, 2), (3, 4)))
        self._check_dgraph(dfs, DGraph([[None, 1], [1, None]], {1}), 0, 1)
        self._check_dgraph(dfs, DGraph([[None, 1, 3], [1, None, 1], [1, 1, None]], {2}), 0, 2)
        # TODO: add tests here!

    def test_ids_output(self):
        self._check_tilegame(ids, ((1, 2, 3), (4, 5, 6), (7, 8, 9)), ((1, 2, 3), (4, 5, 6), (7, 8, 9)), 1)
        self._check_tilegame(ids, ((1, 2), (4, 3)), ((1, 2), (3, 4)), 2)
        self._check_dgraph(ids, DGraph([[None, 1], [1, None]], {1}), 0, 1, 2)
        self._check_dgraph(ids, DGraph([[None, 1, 3], [1, None, 1], [1, 1, None]], {2}), 0, 2, 2)
    #     # TODO: add tests here!

    def test_astar_output(self):
        self._check_tilegame(lambda p: astar(p, lambda s: 0), ((1, 2, 3), (4, 5, 6), (7, 8, 9)), ((1, 2, 3), (4, 5, 6), (7, 8, 9)), 1)
        self._check_tilegame(lambda p: astar(p, lambda s: 0), ((1, 2), (4, 3)), ((1, 2), (3, 4)), 2)
        self._check_dgraph(lambda p: astar(p, lambda s: 0), DGraph([[None, 1], [1, None]], {1}), 0, 1, 2)
        self._check_dgraph(lambda p: astar(p, lambda s: 0), DGraph([[None, 1, 3], [1, None, 1], [1, 1, None]], {2}), 0, 2, 3)
        # TODO: add tests here!

if __name__ == "__main__":
    unittest.main()