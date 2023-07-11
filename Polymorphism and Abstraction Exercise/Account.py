class Account:
    def __init__(self, owner: str, amount=0, transactions=None):
        if transactions is None:
            transactions = []
        self.owner = owner
        self.amount = amount
        self._transactions = transactions

    def handle_transaction(self, transaction_amount):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        else:
            self._transactions.append(transaction_amount)
            return f'New balance: {self.balance}'

    def add_transaction(self, amount):
        if type(amount) != int:
            raise ValueError("please use int for amount")
        else:
            try:
                self.handle_transaction(amount) 
            except ValueError:
                pass

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transactions)

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __iter__(self):
        return iter(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        new_owner = f'{self.owner}&{other.owner}'
        new_amount = self.amount + other.amount
        new_transactions = []
        new_transactions.extend(self._transactions)
        new_transactions.extend(other._transactions)
        return Account(new_owner, new_amount, new_transactions)
