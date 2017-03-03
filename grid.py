import math

class Grid:
    """ Represents the state of the grid """

    def __init__(self, input_state):
        """ Constructs nxn grid of numbered tiles. input_state is an array of integers """

        n = int(math.sqrt(len(input_state)))

        # initialise empty grid
        self.state = [['-' for x in range(n)] for y in range(n)]

        # populate grid with tiles
        i = 0
        j = 0
        for tile in input_state:
            self.state[i][j] = tile
            j += 1
            if j == n:
                j = 0
                i += 1





        

	
