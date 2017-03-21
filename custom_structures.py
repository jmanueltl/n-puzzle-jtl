import Queue

class Custom_Structures:

    # leave __init__ for now. The docs for an abstract class in Python seems
    # overkill for what I want to do here

    # implementing this so I have a custom comparison for Grid objects
    def __contains__(self, item):

        # TODO
        return False



class Frontier(Custom_Structures):
    """docstring for Frontier"""
    
    def __init__(self):
        self.queue = Queue.Queue()

class Explored(Custom_Structures):
    """docstring for Explored"""
    
    def __init__(self):
        self.set = set()
        
    

        
