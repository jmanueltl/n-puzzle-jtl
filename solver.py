import grid


class Solver:
    """ Controller. Takes a grid state, returns path solution """
    
    def __init__(self, input_grid):
        
        self.initial_state = input_grid 

        # queue of grid states
        self.frontier = Queue.queue()

        # set of grid states
        self.explored = set()      



    def breadth_first_search(self):

        initial_grid = grid.Grid(self.initial_state)

        expand_nodes(initial_grid)    

        while not self.frontier.empty():
            state = self.frontier.get()
            self.explored.add(state)

            if goal_test(state):
                return #TODO: what are we returning? do we want the path?

            # add neighbours of this state to the frontier, if not already in the
            # frontier or explored
            expand_nodes(state)


    
    def expand_nodes(self, starting_grid):
        """ adds all possible next nodes from a state to a frontier set """

        for node in ['up', 'down', 'left', 'right']:   

            # need to create new grid object for each node
            # the program is imagining the future!! (maybe change this name...)
            imagined_grid = grid.Grid(starting_grid.state)

            if imagined_grid.move(node):  # returns false if move not possible
                if imagined_grid.state not in self.frontier or self.explored:
                    frontier.put(imagined_grid.state)

        


    def goal_test(state):
        # TODO: implement

        

        




