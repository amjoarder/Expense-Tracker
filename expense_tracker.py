def show_menu():
    print("\n--- Expense Tracker Menu ---")
    print("1. Add an Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("4. Exit")

def add_expense(expenses):
    name = input("Enter the expense name: ").strip()
    try:
        amount = float(input("Enter the expense amount: "))
        expenses.append({"name": name, "amount": amount})
        print(f"Added expense: {name} - ${amount:.2f}")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
    else:
        print("\n--- Recorded Expenses ---")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['name']} - ${expense['amount']:.2f}")

def calculate_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")

def main():
    expenses = []
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
