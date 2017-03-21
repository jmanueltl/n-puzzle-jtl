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
                return #TODO: what are we returning? do we want the path? YES.

            # add neighbours of this state to the frontier, if not already in the
            # frontier or explored
            expand_nodes(state)

        # if we get to here it's gone tits up
        raise ValueError('Shouldn\'t have got to here - gone tits')


    
    def expand_nodes(self, starting_grid):
        """ adds all possible next nodes from a state to a frontier set """

        for node in ['up', 'down', 'left', 'right']:   

            # need to create new grid object for each node
            # the program is imagining the future!! (maybe change this name...)
            imagined_grid = grid.Grid(starting_grid.state)

            if imagined_grid.move(node):  # returns false if move not possible
                # TODO: is this testing strict object equality? don't want that.
                if imagined_grid.state not in self.frontier or self.explored:
                    frontier.put(imagined_grid.state)

        


    def goal_test(state):
        
        # find dimensions of the grid
        height = len(state)
        width = len(state[0])
        if height != width:
            raise ValueError('grid is not a perfect square')
        # note: doesn't test for jagged array (ie. assumes all rows same width)

        # initialise empty grid state
        goal_state = [height][width]

        # populate goal grid with ordered tiles
        # populate grid with tiles
        i = 0
        j = 0
        count = 0
        for tile in :
            goal_state[i][j] = count
            count += 1
            j += 1
            if j == width:
                j = 0
                i += 1

        if state = goal_state:
            return True
        else:
            return False




        

        




