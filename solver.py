import grid


class Solver:
    """ Controller. Takes a grid state, returns path solution """
    
    def __init__(self, input_grid):
        
        self.initial_state = input_grid       



    def breadth_first_search(self):

        initial_grid = grid.Grid(self.initial_state)

        expand_nodes(self.initial_state)    

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

                # TODO: this below is testing object equality. We want value eq.
                if imagined_grid.state not in self.frontier or self.explored:
                    frontier.put(imagined_grid.state)

        


    def goal_test(state):
        # TODO: implement

        

        




