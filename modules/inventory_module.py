from utils.helpers import load_inventory, save_inventory

# Add a new product to the JSON file
def add_product():
    inventory = load_inventory()
    name = input("Product name: ")
    price = int(input("Price: "))
    stock = int(input("Stock quantity: "))
    
    product = {
        "id": len(inventory) + 1,
        "name": name, 
        "price": price,
        "stock": stock
    }
    
    inventory.append(product)
    save_inventory(inventory)
    print(f"✅ Product {name} added successfully.")
    
# Change the stock quantity for an existing product
def update_stock():
    inventory = load_inventory()
    view_stock()
    
    try:
        product_id = int(input("Product id: "))
        new_stock_quantity = int(input("New stock quantity: "))
    except ValueError:
        print("❌ Invalid product ID.")
        return 
        
    for i in inventory:
        if i["id"] == product_id:
            if i["stock"] < new_stock_quantity:
                print("❌ Not enough stock.")
                return
            i["stock"] -= new_stock_quantity
        
            save_inventory(inventory)
            print(f"✅ Stock {new_stock_quantity} units of {i["name"]}. Remaining: {i['stock']}")
    
# Show all products with name, price, and stock.
def view_stock():
    inventory = load_inventory()
    if not inventory:
        print("No stock found.")
        return 
    for i in inventory:
        print(f"ID: [{i['id']}], | Product: {i['name']} | Price: {i['price']} SSP | Stock: {i['stock']}")
        
def inventory_menu():
    while True:
        print("\n📦 Inventory menu")
        print("1. Add Product")
        print("2. Update Stock")
        print("3. View Stock")
        print("0. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == "1":
            add_product()
        elif choice == "2":
            update_stock()
        elif choice == "3":
            view_stock()
        elif choice == "0":
            break 
        else:
            print("❌ Invalid option")