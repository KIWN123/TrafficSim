class Node:
    x_loc, y_loc = None, None

    def __init__(self, x_loc, y_loc):
        self.x_loc = x_loc
        self.y_loc = y_loc

    def get_loc(self):
        return self.x_loc, self.y_loc
        