import math

class Grid:
    """ Represents the state of the grid """

    def __init__(self, input_state):
        """ Constructs n x n grid of numbered tiles. input_state is an array of integers """

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


    def move(self, direction):
        """ 
        Slides a tile in one of 4 directions.
        Returns True if successful (with side-effect of changing the state)
        Returns False if movement in that direction not possible 
        """

        # find coordinates of '0' tile
        zero_coords =  [ (index, row.index('0')) for index, row 
                        in enumerate(self.state) 
                        if '0' in row ]

        # find the offset of the moving tile relative to the '0' tile
        if direction == 'up':
            y, x = 1, 0
        elif direction == 'down':
            y, x = -1, 0
        elif direction == 'left':
            y, x = 0, 1
        elif direction == 'right':
            y, x = 0, -1
        else:
            raise ValueError('Invalid direction: must be \'up\', \'down\', \
                \'left\' or \'right\'')

        # when we say 'move left' we mean the tile, not the space (0) 
        # zero_coords is of form [(y, x)]
        try:  
            tile_to_move = self.state[zero_coords[0][0] + y][zero_coords[0][1] + x]
            self.state[zero_coords[0][0]][zero_coords[0][1]] = tile_to_move
            self.state[zero_coords[0][0] + y][zero_coords[0][1] + x] = '0'
        except IndexError:
            return False

        return True





        

	
