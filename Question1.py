# List of product prices
prices = [25, 60, 45, 100, 55, 30, 80]

# Filter out prices below $50
filtered_prices = list(filter(lambda p: p >= 50, prices))

# Apply 10% discount to the remaining products
discounted_prices = list(map(lambda p: p * 0.9, filtered_prices))

# Display the results
print("Original Prices:", prices)
print("Filtered Prices (>= $50):", filtered_prices)
print("Discounted Prices (10% off):", discounted_prices)
