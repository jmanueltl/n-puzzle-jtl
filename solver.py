import grid
import Queue

class Solver:
    """ Controller. Takes a grid state, returns path solution """
    
    def __init__(self, input_state):
        
        # TODO: are we confusing initial_state here with initial_state in driver.py?
        # different name?
        self.initial_state = grid.Grid(input_state)

    def breadth_first_search(self, input_state):

        # create frontier

        frontier = Queue.Queue()

        for node in ['up', 'down', 'left', 'right']:
            
            # need to create new grid object for each node
            # the program is imagining the future!! (maybe change this name...)
            imagined_grid = grid.Grid(input_state)

            if imagined_grid.move(node):  # returns false if move not possible
                frontier.put(imagined_grid) 

        # test 
        while not frontier.empty():
            print frontier.get().state




