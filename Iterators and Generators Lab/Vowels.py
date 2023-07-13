class vowels:
    def __init__(self, string: str):
        self.string = string
        self.start = 0
        self.end = len(string)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.start < self.end:
                if self.string[self.start].lower() == "a" or self.string[self.start].lower() == "e" or self.string[self.start].lower() == "i" or self.string[self.start].lower() == "u" or self.string[self.start].lower() == "y" or self.string[self.start].lower() == "o":
                    self.start += 1
                    return self.string[self.start - 1]
                else:
                    self.start += 1
            else:
                raise StopIteration
