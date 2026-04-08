# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

# Task 1: Iterate over the products and calculate total sales
for product, values in products.items():
    # Task 2: Convert price to float and quantity sold to int
    price = float(values[0])
    quantity_sold = int(values[1])
    
    # Calculate the total sales for the current product
    total_sales = price * quantity_sold
    
    # Print the total sales for the product
    print(f"Total sales for {product}: ${total_sales}")
    
    # Task 3: Add the total sales to the list
    total_sales_list.append(total_sales)

# Task 4: Calculate and print the total sum of all sales
total_sum = sum(total_sales_list)
print(f"\nTotal sum of all sales: ${total_sum}")

# Task 5: Find and print the minimum and maximum sales
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")