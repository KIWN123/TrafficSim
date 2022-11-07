class Counter:
    num = 0

    def get_num(self):
        return self.num

    def get_and_advance(self):
        self.num += 1
        return self.num