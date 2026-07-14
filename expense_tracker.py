import csv
import os

FILE_NAME="expenses.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME,"w",newline="") as file:
            csv.writer(file).writerow(["Date","Category","Amount","Description"])

def add_expense():
    date=input("Enter Date (DD-MM-YYYY): ")
    category=input("Enter Category: ")
    amount=float(input("Enter Amount: "))
    description=input("Enter Description: ")
    with open(FILE_NAME,"a",newline="") as file:
        csv.writer(file).writerow([date,category,amount,description])
    print("\nExpense Added Successfully!\n")

def view_expenses():
    with open(FILE_NAME,"r") as file:
        for row in csv.reader(file):
            print("{:<15}{:<15}{:<10}{:<20}".format(*row))

def total_expense():
    total=0
    with open(FILE_NAME,"r") as file:
        r=csv.reader(file); next(r)
        for row in r: total+=float(row[2])
    print(f"\nTotal Expense = ₹{total:.2f}\n")

def menu():
    create_file()
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense\n2. View Expenses\n3. Total Expense\n4. Exit")
        c=input("Enter Your Choice: ")
        if c=="1": add_expense()
        elif c=="2": view_expenses()
        elif c=="3": total_expense()
        elif c=="4": break
        else: print("Invalid Choice!")
menu()
