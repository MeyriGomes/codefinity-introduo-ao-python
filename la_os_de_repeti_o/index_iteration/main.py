prices = [29.99, 45.50, 12.75, 38.20]

for index in range(len(prices)):
    original = prices[index]
    if index == 0:
        desconto = 0.10
        updated_price = original * (1 - desconto)
        prices[index] = updated_price
    elif index == 1:
        desconto = 0.20
        updated_price = original * (1 - desconto)
        prices[index] = updated_price
    elif index == 2:
        desconto = 0.15
        updated_price = original * (1 - desconto)
        prices[index] = updated_price
    elif index == 3:
        desconto = 0.05
        updated_price = original * (1 - desconto)
        prices[index] = updated_price
    print(f"Updated price for item {index}: ${updated_price:.2f}")

        