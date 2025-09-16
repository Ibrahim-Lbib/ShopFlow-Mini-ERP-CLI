import json 
import os

# A helper function to read the file
def load_sales():
    if not os.path.exists("data/inventory.json"):
        return
    with open("data/sales.json", "r") as f:
        return json.load(f)
    
def load_inventory():
    if not os.path.exists("data/inventory.json"):
        return []
    with open("data/inventory.json", "r") as f:
        return json.load(f)

def load_debts():
    with open("data/debts.json", "r") as f:
        return json.load(f)
    
def load_expenses():
    with open("data/expenses.json", "r") as f:
        return json.load(f)
    
def count_records(file_path):
    if not os.path.exists(file_path):
        return 0
    with open(file_path, 'r') as f:
        try:
            data = json.load(f)
            return len(data)
        except json.JSONDecodeError: 
            return 0
    
# A helper function to save the file
def save_sales(data):
    with open("data/sales.json", "w") as f:
        json.dump(data, f, indent=4) 

def save_inventory(data):
    with open("data/inventory.json", "w") as f:
        json.dump(data, f, indent=4) 
            
def save_debts(data):
    with open("data/debts.json", "w") as f:
        json.dump(data, f, indent=4)  
    
def save_expenses(data):
    with open("data/expenses.json", "w") as f:
        json.dump(data, f, indent=4)  
        
        