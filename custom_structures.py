from collections import deque
import Queue

class Frontier:
        
    def __init__(self):
        self.queue = deque()

    def __contains__(self, item):
        for element in self.queue:
            if item.state == element.state:
                return True

        return False



class Explored:
       
    def __init__(self):
        self.set = set()

    def __contains__(self, item):
        for element in self.set:
            if item.state == element.state:
                return True

        return False
        
# TODO: this whole difference between Frontier and Priority_Frontier is a messy hack   
class Priority_Frontier:
        
    def __init__(self):
        self.queue = Queue.PriorityQueue()

    def __contains__(self, item):
        for element in self.queue:
            if item.state == element.state:
                return True

        return False
        
