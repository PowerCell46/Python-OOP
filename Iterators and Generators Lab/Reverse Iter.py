class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start = len(iterable) - 1
        self.end = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > -1:
            current_num = self.iterable[self.start]
            self.start -= 1
            return current_num
        else:
            raise StopIteration
