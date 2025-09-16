from modules.sales_module import sales_menu
from modules.inventory_module import inventory_menu
from modules.debt_module import debts_menu
from modules.expense_module import expenses_menu
from reports.report_module import report_menu

def main_menu():
    while True:
        print("\n🏣 ShopFlow Mini ERP")
        print("1. Sales")
        print("2. Inventory")
        print("3. Debts")
        print("4. Expenses")
        print("5. Reports")
        print("0. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            sales_menu()
        elif choice == "2":
            inventory_menu()      
        elif choice == "3":
            debts_menu()      
        elif choice == "4":
            expenses_menu()      
        elif choice == "5":
            report_menu()      
        elif choice == "0":
            print("Exiting ShopFlow. Bye!")
            break 
        else:
            print("❌ Invalid option. Try again.")
                           
if __name__ == "__main__":
    main_menu()           