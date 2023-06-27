class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.dict = list(dictionary.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dict):
            self.index += 1
            return self.dict[self.index - 1]
        else:
            raise StopIteration
