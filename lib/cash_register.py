class CashRegister:
    """Simulates a cash register for an e-commerce site."""

    def __init__(self, discount=0):
        self._discount = discount
        self._total = 0
        self._items = []
        self._previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    @property
    def items(self):
        return self._items

    @property
    def previous_transactions(self):
        return self._previous_transactions

    def add_item(self, title, price, quantity=1):
        """Add an item to the register with optional quantity."""
        transaction_amount = price * quantity
        self._previous_transactions.append(transaction_amount)
        self._total += transaction_amount
        for _ in range(quantity):
            self._items.append(title)

    def apply_discount(self):
        """Apply the discount to the total if one exists."""
        if self._discount > 0:
            self._total = self._total - (self._total * self._discount / 100)
            print(f"After the discount, the total comes to ${self._total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Remove the last transaction amount from the total."""
        if self._previous_transactions:
            last = self._previous_transactions.pop()
            self._total -= last
