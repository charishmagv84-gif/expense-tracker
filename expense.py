class Expense:
    def __init__(self, amount, category, note=""):
        self.amount = amount
        self.category = category
        self.note = note

    def __str__(self):
        return f"{self.category}: Rs.{self.amount} - {self.note}"