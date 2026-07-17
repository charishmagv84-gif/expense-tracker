import json
from datetime import datetime
from expense import Expense

expenses = []
FILENAME = "data.json"

def load_expenses():
    global expenses
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
            expenses = [Expense(item["amount"], item["category"], item["note"]) for item in data]
    except FileNotFoundError:
        expenses = []  # first time running, no file exists yet

def save_expenses():
    data = [{"amount": e.amount, "category": e.category, "note": e.note} for e in expenses]
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    note = input("Enter note (optional): ")
    new_expense = Expense(amount, category, note)
    expenses.append(new_expense)
    save_expenses()
    print("Expense added!")

def view_expenses():
    if not expenses:
        print("No expenses yet.")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e}")

def delete_expense():
    view_expenses()
    if not expenses:
        return
    try:
        index = int(input("Enter the number of the expense to delete: "))
        if 1 <= index <= len(expenses):
            removed = expenses.pop(index - 1)
            save_expenses()
            print(f"Deleted: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def monthly_total():
    total = sum(e.amount for e in expenses)
    print(f"Total expenses: Rs.{total}")

def filter_by_category():
    category = input("Enter category to filter by: ")
    filtered = [e for e in expenses if e.category.lower() == category.lower()]
    if not filtered:
        print("No expenses found in that category.")
    for i, e in enumerate(filtered, start=1):
        print(f"{i}. {e}")

# Load existing data when program starts
load_expenses()

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Expenses")
    print("5. Filter by Category")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        monthly_total()
    elif choice == "5":
        filter_by_category()
    elif choice == "6":
        break
    else:
        print("Invalid choice, try again.")