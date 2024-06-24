def add_expense(expenses):
    while True:
        try:
            category = input("Enter the category of the expense: ").strip()
            amount = float(input("Enter the amount of the expense: ").strip())
            if amount < 0:
                print("Amount cannot be negative. Please try again.")
                continue

            if category in expenses:
                expenses[category].append(amount)
            else:
                expenses[category] = [amount]

            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.")

def calculate_total_expenses(expenses):
    total = 0.0
    for category in expenses:
        total += sum(expenses[category])
    return total

def display_summary(expenses):
    print("\nExpense Summary by Category:")
    for category, amounts in expenses.items():
        total = sum(amounts)
        print(f"{category}: ${total:.2f}")

    total_expenses = calculate_total_expenses(expenses)
    print(f"\nTotal Expenses: ${total_expenses:.2f}")

def main():
    expenses = {}
    print("Welcome to the Expense Tracker!")

    while True:
        print("\n1. Add an expense")
        print("2. Display summary")
        print("3. Exit")

        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_summary(expenses)
        elif choice == '3':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
