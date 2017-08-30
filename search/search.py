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
    """Question 1"""
    visited = []
    stack_DFS = util.Stack()
    currentStateXY = problem.getStartState()
    currentStateAction = []
    stack_DFS.push([currentStateXY,currentStateAction])
    
    while not stack_DFS.isEmpty():
        currentState =  stack_DFS.pop()
        currentStateXY = currentState[0]
        currentStateAction = currentState[1]
        if problem.isGoalState(currentStateXY):
            return currentStateAction
        
        visited.append(currentStateXY)
        successors = problem.getSuccessors(currentStateXY)
        
        for children in successors:
            if children[0] not in visited:
                stack_DFS.push([children[0] ,currentStateAction + [children[1]]])
    return []

def breadthFirstSearch(problem):
    """Question 2"""
    visited = []
    queue_BFS = util.Queue()
    currentStateXY = problem.getStartState()
    currentStateAction = []
    queue_BFS.push([currentStateXY,currentStateAction])

    while not queue_BFS.isEmpty():
        currentState = queue_BFS.pop()
        currentStateXY = currentState[0]
        currentStateAction = currentState[1]
        if problem.isGoalState(currentStateXY):
            return currentStateAction
        
        if currentStateXY not in visited:
            visited.append(currentStateXY)
            successors = problem.getSuccessors(currentStateXY)
            for children in successors:
                queue_BFS.push([children[0] ,currentStateAction + [children[1]]])
    return []

def uniformCostSearch(problem):
    """Question 3"""
    Queue_UCS = util.PriorityQueue()
    currentStateXY = problem.getStartState()
    currentStateAction = []
    currentStateCost = 0
    Queue_UCS.push([currentStateXY,currentStateAction],currentStateCost)
    visited = []

    while not Queue_UCS.isEmpty():
        currentState = Queue_UCS.pop()
        currentStateXY = currentState[0]
        currentStateAction = currentState[1]
        if problem.isGoalState(currentStateXY):
            return currentStateAction
        
        if currentStateXY not in visited:
            visited.append(currentStateXY)
            successors = problem.getSuccessors(currentStateXY)
            for children in successors:
                currentStateXY = children[0]
                allActions = currentStateAction + [children[1]]  
                actionCost = problem.getCostOfActions(allActions)
                Queue_UCS.push((currentStateXY, allActions), actionCost)
    return []

def nullHeuristic(state, problem=None):
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Question 4"""
    Queue_Astar = util.PriorityQueue()
    currentStateXY = problem.getStartState()
    currentStateAction = []
    currentStateCost = 0
    Queue_Astar.push([currentStateXY,currentStateAction, currentStateCost],heuristic(currentStateXY,problem))
    visited = []
    
    while not Queue_Astar.isEmpty():
        currentState = Queue_Astar.pop()
        currentStateXY = currentState[0]
        currentStateAction = currentState[1]
        currentStateCost = currentState[2]
        if problem.isGoalState(currentStateXY):
            return currentStateAction
        
        if currentStateXY not in visited:
            visited.append(currentStateXY)
            successors = problem.getSuccessors(currentStateXY)
            for children in successors:
                currentStateXY = children[0]
                currentDir = children[1]
                currentChildCost = children[2]

                allActions = currentStateAction + [currentDir]
                gN = problem.getCostOfActions(allActions)
                hN = heuristic(currentStateXY,problem)
                AStarTotalCost =  gN + hN 
                Queue_Astar.push((currentStateXY, allActions,gN), AStarTotalCost)
    return []
    
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
