import json
import os
from datetime import datetime

# Function to get user input for expenses
def add_expense(expenses):
    try:
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description of the expense: ")
        category = input("Enter the category (e.g., food, transportation, entertainment): ")
        date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ")
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')
        expenses.append({"amount": amount, "description": description, "category": category, "date": date})
    except ValueError:
        print("Invalid input. Please enter numeric values for the amount.")

# Function to save expenses to a file
def save_expenses(expenses, filename="expenses.json"):
    with open(filename, 'w') as file:
        json.dump(expenses, file, indent=4)

# Function to load expenses from a file
def load_expenses(filename="expenses.json"):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

# Function to display summaries
def summarize_expenses(expenses):
    monthly_summary = {}
    category_summary = {}

    for expense in expenses:
        date = datetime.strptime(expense["date"], '%Y-%m-%d')
        month = date.strftime('%Y-%m')
        amount = expense["amount"]
        category = expense["category"]

        if month not in monthly_summary:
            monthly_summary[month] = 0
        monthly_summary[month] += amount

        if category not in category_summary:
            category_summary[category] = 0
        category_summary[category] += amount

    print("\nMonthly Summary:")
    for month, total in monthly_summary.items():
        print(f"{month}: ${total:.2f}")

    print("\nCategory Summary:")
    for category, total in category_summary.items():
        print(f"{category}: ${total:.2f}")

# Function to display a simple menu
def display_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Save and Exit")

def main():
    expenses = load_expenses()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            summarize_expenses(expenses)
        elif choice == '3':
            save_expenses(expenses)
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
