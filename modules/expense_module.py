from utils.helpers import load_expenses, save_expenses 
from datetime import date 

def add_expense():
    expenses = load_expenses() 
    item = input("What the money was spent on: ")
    amount = int(input("How much was spent: "))
    category = input("Enter category: ")
    
    expense = {
        "id": len(expenses) + 1, 
        "item": item, 
        "amount": amount,
        "category": category,
        "date": date.today().isoformat()
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✅ Expense for {item} added successfully. Amount: {amount:,.2f} SSP | Category: {category}")
    
    
def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expense found.")
        return 
    for e in expenses:
        print(f"ID: [{e['id']}] | Item: {e['item']} | Amount: {e['amount']:,.2f} SSP")
    
def get_total_expenses():
    expenses = load_expenses() 
    if not expenses:
        print("📂 No expenses recorded yet.")
        return 0
    total = sum(expense["amount"] for expense in expenses)
    print(f"💰 Total Expenses: {total:,.2f} SSP")
    return total 


def expenses_menu():
    while True:
        print("\n🧾 Expenses menu")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Get Total Expenses")
        print("0. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == "1":
            add_expense()
        if choice == "2":
            list_expenses()
        if choice == "3":
            get_total_expenses()
        elif choice == "0":
            break 
        else:
            print("❌ Invalid option")    