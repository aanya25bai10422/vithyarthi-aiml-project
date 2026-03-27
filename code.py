# Import the json package
import json

# Attempts to load expenses from a JSON file
def load_expenses(filename):
    try:
        # Open file with "r" read-only capabilites
        with open(filename, "r") as file:
            expenses = json.load(file)
    # Returns empty list if file is not found
    except FileNotFoundError:
        expenses = []
    return expenses

# Saves the current list of expenses to the JSON file
def save_expenses(filename, expenses):
    # Open file with "w" read and write capabilities
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)

# Prompts the user to enter the details for an expense
def add_expense(expenses):
    print("\nEnter Expense Details:")
    name = input("Enter Name: ")
    amount = float(input("Amount: Rs"))
    date = input("Date (YYYY-MM-DD): ")

    # Prompt user for a category
    print("Choose a category:")
    print("1. Food")
    print("2. Transport")
    print("3. Utilites")
    print("4. Entertainment")
    print("5. Miscellaneous")
    category_choice = input("Enter the number for the category: ")

    categories = {
        "1": "Food",
        "2": "Transport",
        "3": "Utilites",
        "4": "Entertainment",
        "5": "Miscellaneous"
    }

    # Get the category based on user input, defaults to "Miscellaneous"
    category = categories.get(category_choice, "Miscellaneous")

    # Create a dictionary to represent the expense
    expense = {
        "name": name,
        "amount": amount,
        "date": date,
        # Add category to the expense
        "category": category
    }

    # Add the expense to the list
    expenses.append(expense)

    print(f"\nExpense added successfully under the category: {category}")

# Show user the expenses if there are any
def view_expenses(expenses):
    # Check for expenses
    if not expenses:
        print("\nNo expenses added yet.")
    else:
        print("\nExpenses:")
        # Loop through the expenses list and print each in a readable format (now including an index)
        for index, expense in enumerate(expenses):
            print(f"{index + 1}. {expense['date']} - {expense['name']}: ${expense['amount']:.2f} [{expense['category']}]")

# Give user ability to edit the expenses listed
def edit_expense(expenses):
    # Show the list of expenses
    view_expenses(expenses)
    try:
        index = int(input("\nEnter the number of the expense you want to edit: ")) - 1
        if 0 <= index < len(expenses):
            print(f"\nEditing {expenses[index]['name']}:")
            name = input("New Name (leave blank to keep the same): ") or expenses[index]['name']
            amount = input(f"New Amount (leave blank to keep ${expenses[index]['amount']}): ") or str(expenses[index]['amount'])
            date = input(f"New Date (leave blank to keep {expenses[index]['date']}): ") or expenses[index]['date']

            print("New Category (leave blank to keep the same):")
            print("1. Food")
            print("2. Transport")
            print("3. Utilites")
            print("4. Entertainment")
            print("5. Miscellaneous")
            category_choice = input("Enter the number for the category: ")

            categories = {
                "1": "Food",
                "2": "Transport",
                "3": "Utilities",
                "4": "Entertainment",
                "5": "Miscellaneous"
            }

            category = categories.get(category_choice, expenses[index]['category'])

            # Update the expense
            expenses[index] = {
                "name": name,
                "amount": float(amount),
                "date": date,
                "category": category
            }
            print("\nExpense updated successfully!")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")

# Gives user the ability to delete an expense
def delete_expenses(expenses):
    # Show the list of expenses
    view_expenses(expenses)
    try:
        index = int(input("\nEnter the number of the expense you want to delete: ")) - 1
        if 0 <= index < len(expenses):
            # Remove expense
            removed_expense = expenses.pop(index)
            print(f"\n{removed_expense['name']} has been deleted.")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    # This will be the name of our file for now
    filename = "expenses.json" ## Would like to add functionality for user to decide between custom or default names
    # Load the expenses from file at the start
    expenses = load_expenses(filename)

    # Runs loop that keeps displaying the menu options until the user chooses the exit (option 3)
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose an option: ")

        # Based on user input, it will call the appropriate function
        if choice == "1":
            # Call the function to add an expense
            add_expense(expenses)
            # Save expenses to the file after adding
            save_expenses(filename, expenses)
        elif choice == "2":
            # Call the function to view expenses
            view_expenses(expenses)
        elif choice == "3":
            # Call the function to edit expenses
            edit_expense(expenses)
            # Save expenses to the file after editing
            save_expenses(filename, expenses)
        elif choice == "4":
            # Call the function to delete expenses
            delete_expenses(expenses)
            # Save expenses to the file after deleting
            save_expenses(filename, expenses)
        elif choice == "5":                     
            print("Goodbye!")
            # Save expenses to the file when exiting
            save_expenses(filename, expenses)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
