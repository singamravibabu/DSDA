# List of products in stock
products_in_stock = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Keyboard",
    "Mouse"
]

# List of sold products
sold_products = []

# List of restocked products
restocked_products = []

# Function to sell a product
def sell_product(product_name):
    if product_name in products_in_stock:
        products_in_stock.remove(product_name)
        sold_products.append(product_name)
        print(f"Sold: {product_name}")
    else:
        print(f"'{product_name}' is not in stock.")

# Function to restock a product
def restock_product(product_name):
    restocked_products.append(product_name)
    products_in_stock.append(product_name)
    print(f"Restocked: {product_name}")

# Function to show current status
def show_inventory():
    print("\nProducts in Stock:", products_in_stock)
    print("Sold Products:", sold_products)
    print("Restocked Products:", restocked_products)

# Real-life usage simulation
show_inventory()
sell_product("Smartphone")
sell_product("Mouse")
show_inventory()
restock_product("Smartphone")
restock_product("Tablet")
show_inventory()
