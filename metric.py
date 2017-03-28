class Metric:

    def __init__(self):

        self.path_to_goal = []

    def cost_of_path(self):
        return len(self.path_to_goal)