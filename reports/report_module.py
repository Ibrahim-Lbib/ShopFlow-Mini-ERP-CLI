from utils.helpers import load_sales
from utils.helpers import load_debts
from utils.helpers import load_expenses 
from utils.helpers import count_records
           
def get_sales_report():
    sales = load_sales()
    num_sales = count_records('data/sales.json') 
    print(f"💰 Total Sales: {num_sales}") 
    total_sales = sum(s["total_price"] for s in sales)
    print(f"💵 Total Sales Amount: {total_sales:,.2f} SSP")
    
def get_debt_report():
    debts = load_debts()
    num_debts = count_records('data/debts.json') 
    print(f"💳 Total Debts: {num_debts}") 
    total_debts = sum(d["total_price"] for d in debts if d["paid"] == False)

def get_expense_report(): 
    expenses = load_expenses()
    num_expenses = count_records('data/expenses.json') 
    print(f"🧾 Total Expenses: {num_expenses}") 
    total_expenses = sum(e["amount"] for e in expenses)
    print(f"💰 Total Expenses Amount: {total_expenses:,.2f}")  

def get_profit_report(): 
    sales = load_sales()
    debts = load_debts()
    expenses = load_expenses()
    
    total_sales = sum(s["total_price"] for s in sales)
    total_debts = sum(d["total_price"] for d in debts if d["paid"] == False)
    total_expenses = sum(e["amount"] for e in expenses)
    
    profit = total_sales - (total_debts + total_expenses)
    
    print(f"📈 Total Profit: {profit:,.2f} SSP") 
    
def report_menu():
    while True:
        print("\n📊 Reports Menu")
        print("1. Get Sales Report")
        print("2. Get Debt Report")
        print("3. Get Expense Report")
        print("4. Get Profit Report")
        print("0. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            get_sales_report()
        if choice == "2":
            get_debt_report()
        if choice == "3":
            get_expense_report()
        if choice == "4":
            get_profit_report()
        elif choice == "0":
            break
        else:
            print("❌ Invalid option.")