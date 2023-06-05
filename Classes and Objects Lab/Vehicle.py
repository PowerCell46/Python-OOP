class Vehicle:
    def __init__(self, *args):
        if len(args) == 2:
            self.max_speed = args[1]
            self.mileage = args[0]
        else:
            self.max_speed = 150
            self.mileage = args[0]
        self.gadgets = []
