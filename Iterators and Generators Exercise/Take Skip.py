class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            self.current_number += self.step
            self.count -= 1
            return self.current_number - self.step
        else:
            raise StopIteration
