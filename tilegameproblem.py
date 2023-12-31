from typing import List, Optional, Tuple
import itertools

import numpy as np

from searchproblem import SearchProblem

# The tile game search problem, implemented as a SearchProblem
# States are board configurations.
# Read the assignment handout for details.

Row = Tuple[int, ...]
TileGameState = Tuple[Row, ...]
LRow = List[int]
TileGameLState = List[LRow]


class TileGame(SearchProblem[TileGameState]):
    def __init__(
        self,
        dim: int,
        start_state: Optional[TileGameState] = None,
        goal_state: Optional[TileGameState] = None,
    ):
        self.__dim = dim
        if start_state == None:
            self.__start_state = TileGame.random_start(dim)
        else:
            self.__start_state = start_state
        if goal_state == None:
            self.goal_state = self.__construct_goal()
        else:
            self.goal_state = goal_state

    ###### SEARCH PROBLEM IMPLEMENTATION ######

    def get_start_state(self):
        return self.__start_state

    def is_goal_state(self, state: TileGameState):
        return state == self.goal_state

    def get_successors(self, state: TileGameState):
        successors = []
        for r in range(self.__dim):
            for c in range(self.__dim):
                if r < self.__dim - 1:
                    successors.append(TileGame.__swap_tiles(state, r, c, r + 1, c))
                if c < self.__dim - 1:
                    successors.append(TileGame.__swap_tiles(state, r, c, r, c + 1))
        costs = itertools.repeat(1)
        return dict(zip(successors, costs))

    ###### INTERNAL HELPER FUNCTIONS ######

    def __construct_goal(self):
        """
        Given the dimension of the tile game, produces the goal state.
        You should not use this function.
        Instead, use is_goal_state to determine if a given state is the goal.
        """
        dim = self.__dim
        return tuple(
            [
                tuple([j + 1 for j in range(dim * i, dim * (i + 1))])
                for i in range(0, dim)
            ]
        )

    @staticmethod
    def __swap_tiles(board, r1, c1, r2, c2):
        """
        Swaps tile at (r1, c1) with tile at (r2, c2) on board. 0 <= r1,r2,c1,c2 < dim
        """
        board = TileGame.tuple_to_list(board)
        board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]
        return TileGame.list_to_tuple(board)

    ###### HELPFUL FUNCTIONS FOR YOU ######

    @staticmethod
    def random_start(dim: int) -> TileGameState:
        """
        Given the dimension, dim, of the tile game, produces a random start state.
        """
        board_arr = (np.random.permutation(dim ** 2) + 1).reshape(dim, dim)
        return TileGame.list_to_tuple(board_arr)

    @staticmethod
    def list_to_tuple(lstate: TileGameLState) -> TileGameState:
        """
        Converts 2D list, lstate, to 2D tuple
        """
        return tuple(map(tuple, lstate))

    @staticmethod
    def tuple_to_list(state: TileGameState) -> TileGameLState:
        """
        Converts 2D tuple, state, to 2D list
        """
        return list(map(list, state))

    @staticmethod
    def board_to_pretty_string(board: TileGameState) -> str:
        """
        Takes in a tile game board, board, and outputs a pretty String representation
        of it for printing.
        """
        hbar = "-"
        vbar = "|"
        corner = "+"
        dim = len(board)

        s = corner
        for i in range(2 * dim - 1):
            s += hbar
        s += corner + "\n"

        for r in range(dim):
            s += vbar
            for c in range(dim):
                s += str(board[r][c]) + " "
            s = s[:-1]
            s += vbar
            s += "\n"

        s += corner
        for i in range(2 * dim - 1):
            s += hbar
        s += corner
        return s

    @staticmethod
    def print_pretty_path(board_path: List[TileGameState]):
        """
        Takes in a list of boards, board_path, and prints them out as
        pretty strings, separated by newlines.
        """
        for b in board_path:
            print(TileGame.board_to_pretty_string(b))
