import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# MySQL Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="expense_tracker"
)

cursor = conn.cursor()

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    cursor.execute(
        "INSERT INTO expenses (expense_date, category, amount, description) VALUES (%s, %s, %s, %s)",
        (date, category, amount, description)
    )

    conn.commit()
    print("Expense added successfully!")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    print("\n--- All Expenses ---")

    for expense in expenses:
        print(expense)

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")

cursor.close()
conn.close()