import csv
import os
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd

FILE = "expenses.csv"


def add_expense():
    date = input("Date (YYYY-MM-DD) [today]: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Category: ").strip()
    description = input("Description: ").strip()

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    file_exists = os.path.exists(FILE)

    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date", "Category", "Description", "Amount"])
        writer.writerow([date, category, description, amount])

    print("Expense added successfully.")


def load_data():
    if not os.path.exists(FILE):
        return pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])

    df = pd.read_csv(FILE)
    if not df.empty:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").fillna(0)
    return df


def view_expenses():
    df = load_data()
    if df.empty:
        print("No expenses found.")
    else:
        print("\nExpense List")
        print(df.to_string(index=False))


def monthly_summary():
    df = load_data()
    if df.empty:
        print("No expenses found.")
        return

    df["Month"] = df["Date"].dt.to_period("M").astype(str)
    summary = df.groupby("Month")["Amount"].sum()

    print("\nMonthly Summary")
    print(summary.to_string())

    summary.plot(kind="bar", title="Monthly Expenses")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()


def category_summary():
    df = load_data()
    if df.empty:
        print("No expenses found.")
        return

    summary = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)

    print("\nCategory Summary")
    print(summary.to_string())

    summary.plot(kind="pie", autopct="%1.1f%%", title="Expenses by Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()


def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you for using Expense Tracker.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
