budget = float(input())
itemCount = 0
itemTotalPrice = 0

while True:
    command = input()
    if command == "Stop":
        print(f"You bought {itemCount} products for {itemTotalPrice:.2f} leva.")
        break

    itemPrice = float(input())
    itemCount = itemCount + 1
    itemTotalPrice = itemTotalPrice + itemPrice / 2 if itemCount % 3 == 0 else itemTotalPrice + itemPrice

    if itemTotalPrice > budget:
        print(f"You don't have enough money!\nYou need {itemTotalPrice - budget:.2f} leva!")
        break