
class CashRegister:
    """Simulates a cash register for an e-commerce site."""

    def __init__(self, employee_discount=None):
        self._employee_discount = employee_discount
        self._total = 0
        self._items = []
        self._last_transaction = 0

    @property
    def employee_discount(self):
        return self._employee_discount

    @property
    def total(self):
        return self._total

    @property
    def items(self):
        return self._items

    def add_item(self, title, price, quantity=1):
        """Add an item to the register with optional quantity."""
        transaction_amount = price * quantity
        self._last_transaction = transaction_amount
        self._total += transaction_amount
        for _ in range(quantity):
            self._items.append(title)

    def apply_discount(self):
        """Apply the employee discount to the total if one exists."""
        if self._employee_discount:
            self._total = int(self._total - (self._total * self._employee_discount / 100))
            return f"After the discount, the total comes to ${self._total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        """Remove the last transaction amount from the total."""
        self._total -= self._last_transaction
        self._last_transaction = 0