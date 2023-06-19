class Account:
    def __init__(self, id: int, balance: int, pin: int):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        else:
            return f'Wrong pin'

    def change_pin(self, old, new):
        if old == self.__pin:
            self.__pin = new
            return 'Pin changed'
        else:
            return f'Wrong pin'
