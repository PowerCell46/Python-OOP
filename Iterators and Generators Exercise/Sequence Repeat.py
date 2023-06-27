class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.length = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.length < self.number:
            self.length += 1
            self.index += 1
            if self.index - 1 == len(self.sequence):
                self.index = 1
            return self.sequence[self.index - 1]
        else:
            raise StopIteration
