from depreciated.basicobj import BasicObj

class Tile(BasicObj):
    def __init__(self, counter, x, y, map):
        #super(Tile, self).__init__(counter)
        super().__init__(counter)
        self.x = x
        self.y = y

        self.id = str(super().GetID())
        map[x][y] = "T" + self.id


    def GetCoords(self):
        return (self.x, self.y)
