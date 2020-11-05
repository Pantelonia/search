# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    childs = problem.getSuccessors(problem.getStartState())
    print "Start's successors:", childs
    firstChild = childs[0]
    print "second successors:", problem.getSuccessors(firstChild[0])
    """
    "*** YOUR CODE HERE ***"
    "Initiate primary variables"
    stack = util.Stack()
    current_position = problem.getStartState()
    visited = []
    route = []
    stack.push((current_position, route))

    while not stack.isEmpty() and not problem.isGoalState(current_position):
        state, actions = stack.pop()
        visited.append(state)
        children = problem.getSuccessors(state)
        for child in children:
            coordinates = child[0]
            if not coordinates in visited:
                current_position = coordinates
                direction = child[1]
                stack.push((coordinates, actions + [direction]))
    return actions + [direction]
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    current_position = problem.getStartState()
    visited = []
    visited.append(current_position)
    queue.push((current_position, []))
    while not queue.isEmpty():
        state, action = queue.pop()
        if problem.isGoalState(state):
            return action
        children = problem.getSuccessors(state)
        for child in children:
            coordinates = child[0]
            if not coordinates in visited:
                direction = child[1]
                visited.append(coordinates)
                queue.push((coordinates, action + [direction]))
    return action
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    current_position = problem.getStartState()
    visited = []
    queue = util.PriorityQueue()
    queue.push((current_position, []) ,0)
    while not queue.isEmpty():
        state, actions = queue.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            successors = problem.getSuccessors(state)
            for i in successors:
                coordinates = i[0]
                if coordinates not in visited:
                    direction = i[1]
                    actCost = actions + [direction]
                    queue.push((coordinates, actions + [direction]), problem.getCostOfActions(actCost))
        visited.append(state)
    return actions
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    priority_queue = util.PriorityQueue()
    current_position = problem.getStartState()
    priority_queue.push((current_position, []), nullHeuristic(current_position, problem))
    cost_so_far = 0
    visited = []
    while not priority_queue.isEmpty():
        state, action = priority_queue.pop()
        if problem.isGoalState(state):
            return action
        if state not in visited:
        	visited.append(state)
        	successors = problem.getSuccessors(state)
        	for child in successors:
        		coordinates = child[0]
        		if coordinates not in visited:
        			direction = child[1]
        			new_action = action + [direction]
        			cost_so_far = problem.getCostOfActions(new_action) + heuristic(coordinates, problem)
        			priority_queue.push((coordinates, new_action), cost_so_far)
    return action
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
