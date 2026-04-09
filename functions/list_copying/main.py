def apply_discount(prices):
    # Create a copy so the original list isn’t modified
    prices_copy = prices.copy()
    
    # Iterate by index to update values in place
    for index in range(len(prices_copy)):
        if prices_copy[index] > 2.00:
            prices_copy[index] *= 0.90  # apply 10% discount
    
    return prices_copy

# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

# Print the updated prices
print(f"Updated product prices: {updated_prices}")