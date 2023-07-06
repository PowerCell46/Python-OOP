class Stack:
    def __init__(self,):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) > 0:
            return False
        else:
            return True

    def __str__(self):
        reversed_list = self.data
        reversed_list = reversed_list[::-1]
        return "[" + ", ".join([str(el) for el in reversed_list]) + "]"
