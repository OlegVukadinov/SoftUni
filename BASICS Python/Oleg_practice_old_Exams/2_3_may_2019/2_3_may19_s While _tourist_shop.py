budget = float(input())

total_price_of_product = 0
product_counter = 0
name_of_product = input()

while name_of_product != "Stop":

    price_of_product = float(input())

    if (product_counter + 1) % 3 == 0:
        price_of_product = price_of_product / 2

    if price_of_product > budget:
        print("You don't have enough money!")
        print(f"You need {(price_of_product - budget):.2f} leva!")
        break

    product_counter += 1

    budget -= price_of_product

    total_price_of_product += price_of_product

    name_of_product = input()

if name_of_product == "Stop":
    print(f"You bought {product_counter} products for {total_price_of_product:.2f} leva.")


