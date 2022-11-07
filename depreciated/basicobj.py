import count

class BasicObj:
    def __init__(self, counter):
        self._id = counter.num
        counter.num += 1

    def GetID(self):
        return self._id

