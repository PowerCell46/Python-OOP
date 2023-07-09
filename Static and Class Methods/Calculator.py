class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        res = 1
        for el in args:
            res *= el
        return res

    @staticmethod
    def divide(*args):
        res = args[0]
        for index in range(1, len(args)):
            res /= args[index]
        return res

    @staticmethod
    def subtract(*args):
        res = args[0]
        for index in range(1, len(args)):
            res -= args[index]
        return res

