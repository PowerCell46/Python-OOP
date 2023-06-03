class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        free_space = self.size - self.quantity
        if quantity <= free_space:
            self.quantity += quantity

    def status(self):
        return self.size - self.quantity
