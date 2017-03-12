import grid
import Queue

class Solver:
    """ Controller. Takes a grid state, returns path solution """
    
    def __init__(self, input_state):
        
        # TODO: are we confusing initial_state here with initial_state in driver.py?
        # different name?
        self.initial_state = grid.Grid(input_state)

        self.frontier = Queue.Queue()

        self.explored = set()



    def breadth_first_search(self, input_state):

        expand_nodes(input_state)    

        while not frontier.empty():
            state = frontier.get()
            explored.add(state)

            if goal_test(state):
                return #TODO: what are we returning? do we want the path?

            # add neighbours of this state to the frontier, if not already in the
            # frontier or explored
            expand_nodes(state)


    
    def expand_nodes(self, state):
        """ adds all possible next nodes from a state to a frontier set """

        for node in ['up', 'down', 'left', 'right']:   

            # need to create new grid object for each node
            # the program is imagining the future!! (maybe change this name...)
            imagined_grid = grid.Grid(state)

            if imagined_grid.move(node):  # returns false if move not possible
                if imagined_grid.state not in self.frontier or self.explored:
                    frontier.put(imagined_grid.state)

        


    def goal_test(state):
        # TODO: implement

        # TODO: we have three different 'states' being passed around:
        # input_state, the grid object, and the state property of the grid
        # object. Think + clean this up

        




