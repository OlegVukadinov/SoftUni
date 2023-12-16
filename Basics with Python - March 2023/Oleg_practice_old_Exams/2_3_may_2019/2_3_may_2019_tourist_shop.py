budget = float(input())
counter_num_products = 0
counter_spent_money = 0

while True:
    product_name = input()
    if product_name == "Stop":
        print(f"You bought {counter_num_products} products for {counter_spent_money:.2f} leva.")
        break

    product_price = float(input())
    counter_num_products += 1
    if counter_num_products % 3 == 0:
        product_price = product_price / 2

    if product_price > budget:
        print("You don't have enough money!")
        print(f"You need {(product_price - budget):.2f} leva!")
        break

    budget -= product_price
    counter_spent_money += product_price
