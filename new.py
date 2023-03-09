import csv
from datetime import datetime

# Function to record expense
def record_expense(amount, category):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("expenses.csv", mode="a") as expense_file:
        expense_writer = csv.writer(expense_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        expense_writer.writerow([date, amount, category])
    print("Expense recorded successfully!")

# Function to display expenses
def display_expenses():
    with open("expenses.csv", mode="r") as expense_file:
        expense_reader = csv.reader(expense_file, delimiter=",")
        for row in expense_reader:
            print(row)

# Create loop to record expenses
while True:
    print("Enter expense details: ")
    amount = input("Amount: ")
    category = input("Category: ")
    record_expense(amount, category)
    choice = input("Do you want to record another expense? (y/n): ")
    if choice.lower() == "n":
        break

# Display all expenses
print("All expenses:")
display_expenses()