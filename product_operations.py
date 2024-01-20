def calculate_discounted_total(basket, product_prices):
    total_cost = 0

    # Calculate total cost of the basket
    for product, quantity in basket.items():
        if product in product_prices:
            total_cost += quantity * product_prices[product]
        else:
            print(f"Warning: Product '{product}' not found in the price list.")

    # Apply a 10% discount
    discounted_total = total_cost * 0.9

    return discounted_total

# Example usage
product_prices = {
    'apple': 1.0,
    'banana': 0.7,
    'orange': 1.2,
    'grapes': 2.5
}

basket = {
    'apple': 3,
    'banana': 2,
    'grapes': 1
}

discounted_total = calculate_discounted_total(basket, product_prices)

print(f"Total cost before discount: ${sum(basket[product] * product_prices[product] for product in basket)}")
print(f"Discounted total cost: ${discounted_total:.2f}")
