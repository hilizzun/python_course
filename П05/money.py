from decimal import Decimal

class Money:

    def __init__(self, amount, currency):
        if currency is None:
            raise ValueError("currency cannot be None")
        self.amount = Decimal(str(amount))
        self.currency = currency

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("currency mismatch")
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __hash__(self):
        return hash((self.amount, self.currency))

    def __repr__(self):
        return f"Money({self.amount}, {self.currency!r})"