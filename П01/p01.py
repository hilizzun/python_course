class Account:
    def __init__(self, initial):
        if initial < 0:
            raise ValueError("initial must be non-negative")
        self.__balance = initial

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.__balance:
            raise RuntimeError("insufficient funds")
        self.__balance -= amount
