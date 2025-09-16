from utils.helpers import load_inventory, save_inventory, load_debts, save_debts
from datetime import date

# Record a credit sale. 
def add_debt():
    debts = load_debts() 
    inventory = load_inventory()
    customer = input("Customer name: ")  
    product_id = int(input("Product ID: ")) 
    quantity_sold = int(input("Quantity sold: "))
    product = next((p for p in inventory if p["id"] == product_id), None)
    if not product:
        print("❌ Product not found.")
        return
    if quantity_sold > product["stock"]:
        print(f"❌ Not enough stock. Available: {product['stock']}")
        return
    total_price = product["stock"] * quantity_sold
    
    debt = {
        "id": len(debts) + 1, 
        "customer": customer,
        "product_id": product_id,
        "quantity_sold": quantity_sold,
        "total_price": total_price,
        "paid": False,
        "date": date.today().isoformat()
    }
    
    debts.append(debt)
    save_debts(debts)
    
    product["stock"] -= quantity_sold
    save_inventory(inventory)
    print(f"✅ Debt for {product['name']} added successfully. Total: {total_price:,.2f} SSP")
    
# List all unpaid debts. 
def view_debts():
    debts = load_debts()
    paid = False 
    if not debts:
        print("No debt found.")
        return
    if paid == False:
        for d in debts:
            print(f"ID: {d['id']} | Customer: {d['customer']} | Amount: {d['total_price']}")
        
# Update a record to show it's paid. 
def mark_as_paid():
    debts = load_debts()
    view_debts()
    debt_id = int(input("Enter Debt ID to mark as paid: "))
    debt = next((d for d in debts if d['id'] == debt_id), None)
    if not debt:
        print("❌ Debt not found.")
        return
    if debt['paid']:
        print("⚠️ This debt is already marked as paid.")    
        return
    
    debt['paid'] = True
    save_debts(debts)
    print(f"✅ Debt ID {debt_id} has been marked as paid.")          
    
def debts_menu():
    while True:     
        print("\n💸 Debt menu")
        print("1. Add Debt")
        print("2. View Debts")
        print("3. Mark as Paid")
        print("0. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == "1":
            add_debt()
        elif choice == "2":
            view_debts()
        elif choice == "3":
            mark_as_paid()
        elif choice == "0":
            break 
        else:
            print("❌ Invalid option")