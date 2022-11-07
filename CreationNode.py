class CreationNode:
    def __init__(self, x_loc, y_loc, id):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.next = None
        self.id = id
        print(x_loc, y_loc)

    def get_loc(self):
        return self.x_loc, self.y_loc

    def get_id(self):
        return self.id
        