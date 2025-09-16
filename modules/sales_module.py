from utils.helpers import load_sales, save_sales, load_inventory, save_inventory
from datetime import date
       
# Add a new sale 
def add_sale():
    sales = load_sales()
    inventory = load_inventory()
    view_sales()
    product_id = int(input("Product ID: "))
    quantity = int(input("Quantitiy sold: "))
    product = next((p for p in inventory if p["id"] == product_id), None)
    if not product:
        print("❌ Product not found.")
        return
    if quantity > product["stock"]:
        print(f"❌ Not enough stock. Available: {product['stock']}")
        return
    total_price = product["stock"] * quantity
    
    sale = {
        "id": len(sales) + 1,
        "product_id": product_id,
        "quantity": quantity,
        "total_price": total_price,
        "date": date.today().isoformat()
    }
    
    sales.append(sale)
    save_sales(sales)
    
    product["stock"] -= quantity
    save_inventory(inventory)
    print(f"✅ Sale for {product['name']} added successfully. Total: {total_price}")
    
# Show all products with name, price, and stock.
def view_sales():
    sales = load_sales()
    if not sales:
        print("No stock found.")
        return 
    for s in sales:
        print(f"ID: [{s['id']}] | Product: {s['product_id']} | Quantity: {s['quantity']} | Total: {s['total_price']}")
        
def sales_menu():
    while True:
        print("\n💵 Sales menu")
        print("1. Add Sale")
        print("2. View Today's Sale")
        print("0. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == "1":
            add_sale()
        elif choice == "2":
            view_sales()
        elif choice == "0":
            break 
        else:
            print("❌ Invalid option")