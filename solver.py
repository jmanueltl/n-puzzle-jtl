import grid
import Queue

class Solver:
    """ Controller. Takes a grid state, returns path solution """
    
    def __init__(self, input_state):
        
        # TODO: are we confusing initial_state here with initial_state in driver.py?
        # different name?
        self.initial_state = grid.Grid(input_state)



    def breadth_first_search(self, input_state):

        # create frontier: next nodes to search
        frontier = Queue.Queue()
        expand_nodes(frontier, input_state)
          

        # keep track of nodes already visited
        explored = set()

        while not frontier.empty():
            state = frontier.get()
            explored.add(state)

            if goal_test(state):
                return #TODO: what are we returning? do we want the path?

            # add neighbours of this state to the frontier, if not already in the
            # frontier or explored
            # TODO


    def expand_nodes(frontier, state):
        """ adds all possible next nodes from a state to a frontier set """

        for node in ['up', 'down', 'left', 'right']:   

            # need to create new grid object for each node
            # the program is imagining the future!! (maybe change this name...)
            imagined_grid = grid.Grid(input_state)

            if imagined_grid.move(node):  # returns false if move not possible
                # add the state (a list) rather than the whole object, as may run 
                # into problems later testing equality of objects
                frontier.put(imagined_grid.state)

        # TODO: we can modify the passed frontier because the lists in the queue
        # are mutable. However, it may be a clearer pattern to have this function
        # as a method of the frontier object
        # see http://softwareengineering.stackexchange.com/questions/262221/coding-style-issue-should-we-have-functions-which-take-a-parameter-modify-it



    def goal_test(state):
        # TODO: implement

        # TODO: we have three different 'states' being passed around:
        # input_state, the grid object, and the state property of the grid
        # object. Think + clean this up

        




