# NOTE TO STUDENT: Please read the handout before continuing.

from math import inf
from queue import LifoQueue, PriorityQueue, Queue
from typing import Callable, List

from numpy import integer

from dgraph import DGraph
from searchproblem import SearchProblem, State
from tilegameproblem import TileGame, TileGameState


### GENERAL SEARCH IMPLEMENTATIONS - NOT SPECIFIC TO THE TILEGAME PROBLEM ###


def traceback(parent, start, goal)->List[State]:
    """
    backtraces a state from current state all the way to the root, i.e. the 
    start state.

    Input:
        parent - a hashset containing a key from node to the parent
        start - the state of the root node
        goal - the target node

    Output: A list of states representing the path from start to goal
    """
    route = [goal]
    while route[-1] != start:
        route.append(parent[route[-1]])
    route.reverse()
    return route


def bfs(problem: SearchProblem[State]) -> List[State]:
    """
    Implement breadth-first search.

    Input:
        problem - the problem on which the search is conducted, a SearchProblem

    Output: a list of states representing the path of the solution

    """
    frontier = Queue()
    frontier.put(problem.get_start_state)
    visited = {}
    while not (frontier.empty()):
        node = frontier.get()
        if problem.is_goal_state(node):
            return traceback(visited, problem.get_start_state, node)
        for child in problem.get_successors(node):
            if child not in visited:
                visited[child] = node
                frontier.put(child)
    return []



def dfs(problem: SearchProblem[State]) -> List[State]:
    """
    Implement depth-first search.

    Input:
        problem - the problem on which the search is conducted, a SearchProblem

    Output: a list of states representing the path of the solution

    """
    frontier = LifoQueue()
    frontier.put(problem.get_start_state)
    visited = {}
    while not (frontier.empty()):
        node = frontier.get()
        if problem.is_goal_state(node):
            return traceback(visited, problem.get_start_state, node)
        for child in problem.get_successors(node):
            if child not in visited:
                visited[child] = node
                frontier.put(child)
    return []


def DLS(problem: SearchProblem[State], depth: integer):
    node = problem.get_start_state
    frontier = LifoQueue()
    frontier.put(node)
    visited = {}
    recordDepth = {}
    depth = {problem.get_start_state : 0}
    while not (frontier.empty()):
        node = frontier.get()
        if problem.is_goal_state(node):
            return traceback(visited, problem.get_start_state, node)
        # value of the node id Record Depth is less than the depth then compute
        if recordDepth[node] < depth:
            for child in problem.get_successors(node):
                if child not in visited:
                    visited[child] = node
                    recordDepth[child] = recordDepth[node] + 1
                    frontier.put(child)
    return []

def ids(problem: SearchProblem[State]) -> List[State]:
    """
    Implement iterative deepening search.

    Input:
        problem - the problem on which the search is conducted, a SearchProblem

    Output: a list of states representing the path of the solution

    """
    for depth in range(float(inf)):
        result = DLS(problem, depth)
        if result != []:
            return result


def astar(problem: SearchProblem[State], heur: Callable[[State], float]) -> List[State]:
    """
    Implement A* search.

    The given heuristic function will take in a state of the search problem
    and produce a real number.

    Your implementation should be able to work with any heuristic
    that is for the given search problem (but, of course, without a
    guarantee of optimality if the heuristic is not admissible).

    Input:
        problem - the problem on which the search is conducted, a SearchProblem
        heur - a heuristic function that takes in a state as input and outputs a number

    Output: a list of states representing the path of the solution

    """
    ...


### SPECIFIC TO THE TILEGAME PROBLEM ###


def tilegame_heuristic(state: TileGameState) -> float:
    """
    Produces a number for the given tile game state representing
    an estimate of the cost to get to the goal state. Remember that this heuristic must be
    admissible, that is it should never overestimate the cost to reach the goal.
    Input:
        state - the tilegame state to evaluate. Consult handout for how the tilegame state is represented

    Output: a float.

    """
    ...


### YOUR SANDBOX ###


def main():
    """
    Do whatever you want in here; this is for you.
    The examples below shows how your functions might be used.
    """

    # initialize a random 3x3 TileGame problem
    tg = TileGame(3)
    # print(TileGame.board_to_pretty_string(tg.get_start_state()))
    # compute path using dfs
    path = dfs(tg)
    # display path
    TileGame.print_pretty_path(path)

    # initialize a small DGraph
    small_dgraph = DGraph([[None, 1], [1, None]], {1})
    # print the path using ids
    print(ids(small_dgraph))


if __name__ == "__main__":
    main()
