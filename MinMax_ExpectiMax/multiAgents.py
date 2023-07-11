# multiAgents.py
# --------------
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


from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        #return successorGameState.getScore()
        food = currentGameState.getFood()
        currentPos = list(successorGameState.getPacmanPosition())
        distance = float("-Inf")

        foodList = food.asList()

        if action == 'Stop':
            return float("-Inf")

        for state in newGhostStates:
            if state.getPosition() == tuple(currentPos) and (state.scaredTimer == 0):
                return float("-Inf")

        for x in foodList:
            tempDistance = -1 * (util.manhattanDistance(currentPos, x))
            if (tempDistance > distance):
                distance = tempDistance

        return distance


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'betterEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        def alphabeta(state):
            bestValue, bestAction = None, None
            print(state.getLegalActions(0))
            value = []
            for action in state.getLegalActions(0):
                #value = max(value,minValue(state.generateSuccessor(0, action), 1, 1))
                succ  = minValue(state.generateSuccessor(0, action), 1, 1)
                value.append(succ)
                if bestValue is None:
                    bestValue = succ
                    bestAction = action
                else:
                    if succ > bestValue:
                        bestValue = succ
                        bestAction = action
            print(value)
            return bestAction

        def minValue(state, agentIdx, depth):
            if agentIdx == state.getNumAgents():
                return maxValue(state, 0, depth + 1)
            value = None
            for action in state.getLegalActions(agentIdx):
                succ = minValue(state.generateSuccessor(agentIdx, action), agentIdx + 1, depth)
                if value is None:
                    value = succ
                else:
                    value = min(value, succ)

            if value is not None:
                return value
            else:
                return self.evaluationFunction(state)


        def maxValue(state, agentIdx, depth):
            if depth > self.depth:
                return self.evaluationFunction(state)
            value = None
            for action in state.getLegalActions(agentIdx):
                succ = minValue(state.generateSuccessor(agentIdx, action), agentIdx + 1, depth)
                if value is None:
                    value = succ
                else:
                    value = max(value, succ)
                
            if value is not None:
                return value
            else:
                return self.evaluationFunction(state)

        action = alphabeta(gameState)

        return action

        # def minimax_search(state, agentIndex, depth):
        #     # if in min layer and last ghost
        #     if agentIndex == state.getNumAgents():
        #         # if reached max depth, evaluate state
        #         if depth == self.depth:
        #             return self.evaluationFunction(state)
        #         # otherwise start new max layer with bigger depth
        #         else:
        #             return minimax_search(state, 0, depth + 1)
        #     # if not min layer and last ghost
        #     else:
        #         moves = state.getLegalActions(agentIndex)
        #         # if nothing can be done, evaluate the state
        #         if len(moves) == 0:
        #             return self.evaluationFunction(state)
        #         # get all the minimax values for the next layer with each node being a possible state after a move
        #         next = (minimax_search(state.generateSuccessor(agentIndex, m), agentIndex + 1, depth) for m in moves)

        #         # if max layer, return max of layer below
        #         if agentIndex == 0:
        #             return max(next)
        #         # if min layer, return min of layer below
        #         else:
        #             return min(next)
        # # select the action with the greatest minimax value
        # result = max(gameState.getLegalActions(0), key=lambda x: minimax_search(gameState.generateSuccessor(0, x), 1, 1))

        # return result        

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        result = self.getBestActionAndScore(gameState, 0, 0, float("-inf"), float("inf"))
        return result[0]
    def getBestActionAndScore(self, game_state, index, depth, alpha, beta):
        """
        Returns value as pair of [action, score] based on the different cases:
        1. Terminal state
        2. Max-agent
        3. Min-agent
        """
        # Terminal states:
        if len(game_state.getLegalActions(index)) == 0 or depth == self.depth:
            return "", game_state.getScore()

        # Max-agent: Pacman has index = 0
        if index == 0:
            return self.max_value(game_state, index, depth, alpha, beta)

        # Min-agent: Ghost has index > 0
        else:
            return self.min_value(game_state, index, depth, alpha, beta)

    def max_value(self, game_state, index, depth, alpha, beta):
        """
        Returns the max utility action-score for max-agent with alpha-beta pruning
        """
        legalMoves = game_state.getLegalActions(index)
        max_value = float("-inf")
        max_action = ""

        for action in legalMoves:
            successor = game_state.generateSuccessor(index, action)
            successor_index = index + 1
            successor_depth = depth

            # Update the successor agent's index and depth if it's pacman
            if successor_index == game_state.getNumAgents():
                successor_index = 0
                successor_depth += 1

            # Calculate the action-score for the current successor
            current_action, current_value \
                = self.getBestActionAndScore(successor, successor_index, successor_depth, alpha, beta)

            # Update max_value and max_action for maximizer agent
            if current_value > max_value:
                max_value = current_value
                max_action = action

            # Update alpha value for current maximizer
            alpha = max(alpha, max_value)

            # Pruning: Returns max_value because next possible max_value(s) of maximizer
            # can get worse for beta value of minimizer when coming back up
            if max_value > beta:
                return max_action, max_value

        return max_action, max_value

    def min_value(self, game_state, index, depth, alpha, beta):
        """
        Returns the min utility action-score for min-agent with alpha-beta pruning
        """
        legalMoves = game_state.getLegalActions(index)
        min_value = float("inf")
        min_action = ""

        for action in legalMoves:
            successor = game_state.generateSuccessor(index, action)
            successor_index = index + 1
            successor_depth = depth

            # Update the successor agent's index and depth if it's pacman
            if successor_index == game_state.getNumAgents():
                successor_index = 0
                successor_depth += 1

            # Calculate the action-score for the current successor
            current_action, current_value \
                = self.getBestActionAndScore(successor, successor_index, successor_depth, alpha, beta)

            # Update min_value and min_action for minimizer agent
            if current_value < min_value:
                min_value = current_value
                min_action = action

            # Update beta value for current minimizer
            beta = min(beta, min_value)

            # Pruning: Returns min_value because next possible min_value(s) of minimizer
            # can get worse for alpha value of maximizer when coming back up
            if min_value < alpha:
                return min_action, min_value

        return min_action, min_value


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        action, score = self.get_value(gameState, 0, 0)

        return action
    def get_value(self, game_state, index, depth):
        """
        Returns value as pair of [action, score] based on the different cases:
        1. Terminal state
        2. Max-agent
        3. Expectation-agent
        """
        # Terminal states:
        if len(game_state.getLegalActions(index)) == 0 or depth == self.depth:
            return "", self.evaluationFunction(game_state)

        # Max-agent: Pacman has index = 0
        if index == 0:
            return self.max_value(game_state, index, depth)

        # Expectation-agent: Ghost has index > 0
        else:
            return self.expected_value(game_state, index, depth)

    def max_value(self, game_state, index, depth):
        """
        Returns the max utility value-action for max-agent
        """
        legalMoves = game_state.getLegalActions(index)
        max_value = float("-inf")
        max_action = ""

        for action in legalMoves:
            successor = game_state.generateSuccessor(index, action)
            successor_index = index + 1
            successor_depth = depth

            # Update the successor agent's index and depth if it's pacman
            if successor_index == game_state.getNumAgents():
                successor_index = 0
                successor_depth += 1

            current_action, current_value = self.get_value(successor, successor_index, successor_depth)

            if current_value > max_value:
                max_value = current_value
                max_action = action

        return max_action, max_value

    def expected_value(self, game_state, index, depth):
        """
        Returns the max utility value-action for max-agent
        """
        legalMoves = game_state.getLegalActions(index)
        expected_value = 0
        expected_action = ""

        # Find the current successor's probability using a uniform distribution
        successor_probability = 1.0 / len(legalMoves)

        for action in legalMoves:
            successor = game_state.generateSuccessor(index, action)
            successor_index = index + 1
            successor_depth = depth

            # Update the successor agent's index and depth if it's pacman
            if successor_index == game_state.getNumAgents():
                successor_index = 0
                successor_depth += 1

            # Calculate the action-score for the current successor
            current_action, current_value = self.get_value(successor, successor_index, successor_depth)

            # Update expected_value with the current_value and successor_probability
            expected_value += successor_probability * current_value

        return expected_action, expected_value





def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    ##util.raiseNotDefined()
    #newPos = currentGameState.getPacmanPosition()
    #newFood = currentGameState.getFood()
    #newGhostStates = currentGameState.getGhostStates()
    #newCapsules = currentGameState.getCapsules()
    #newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    #closestGhost = min([util.manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates])
    #if newCapsules:
    #    closestCapsule = min([util.manhattanDistance(newPos, caps) for caps in newCapsules])
    #else:
    #    closestCapsule = 0

    #if closestCapsule:
    #    closest_capsule = -3 / closestCapsule
    #else:
    #    closest_capsule = 100

    #if closestGhost:
    #    ghost_distance = -2 / closestGhost
    #else:
    #    ghost_distance = -500

    #foodList = newFood.asList()
    #if foodList:
    #    closestFood = min([util.manhattanDistance(newPos, food) for food in foodList])
    #else:
    #    closestFood = 0

    #return -2 * closestFood + ghost_distance - 10 * len(foodList) + closest_capsule

    #_________________________________________________________________________________________
    # Ưu tiên thắng
    if currentGameState.isWin():
        return float("+inf")
  
    # Tránh bị thua
    if currentGameState.isLose():
        return float("-inf")

    # Lấy các biến cần thiết (điểm lượng giá, danh sách điểm thức ăn, vị trí Pacman, vị trí các con ma)
    score = scoreEvaluationFunction(currentGameState)
    newFoodList = currentGameState.getFood().asList()
    newPos = currentGameState.getPacmanPosition()
    GhostPos = currentGameState.getGhostPositions()      
  
    # Tính khoảng cách đến điểm thức ăn gần nhất
    if(len(newFoodList) != 1):
        minDistanceFood = float("+Inf")
        for foodPos in newFoodList:
            minDistanceFood = min(minDistanceFood, util.manhattanDistance(foodPos, newPos))
    else:
        minDistanceFood = util.manhattanDistance(newFoodList[0], newPos)
    
    #print(newFoodList)

    # Tình khoảng cách đến vị trí mấy con ma
    for ghost_position in GhostPos:
        ghost_distance = util.manhattanDistance(newPos, ghost_position)

        # Nếu ma ở gần, ưu tiên chạy đến viên năng lượng
        if ghost_distance < 4:
            # ưu tiên chạy đến vị trí điểm năng lượng
            capsulelocations = currentGameState.getCapsules()
            score -= 4 * len(capsulelocations)
        else: 
            # Ưu tiên ăn thức ăn
            score -= 4 * len(newFoodList)
            # Ưu tiên chạy đến điểm thức ăn gần nhất
            score -= 2 * minDistanceFood

      
    # Ưu tiên chạy đến điểm thức ăn gần nhất
    score -= 2 * minDistanceFood
  
    # Ưu tiên ăn thức ăn
    score -= 4 * len(newFoodList)
  
    features = [1.0 / minDistanceFood,
                score,
                len(newFoodList),
                len(currentGameState.getCapsules())]

    weights = [10,
               200,
               -100,
               -10]
  
    #return sum([feature * weight for feature, weight in zip(features, weights)])
    return score

# Abbreviation
better = betterEvaluationFunction
