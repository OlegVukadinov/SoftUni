start_eggs_in_shop = int(input())

counter_eggs = start_eggs_in_shop
counter_sold_eggs = 0

command = input()

while command != "Close":
    number_eggs = int(input())

    if command == "Fill":
        counter_eggs += number_eggs

    if number_eggs > counter_eggs:
        print("Not enough eggs in store!")
        print(f"You can buy only {counter_eggs}.")
        break

    if command == "Buy":
        counter_eggs -= number_eggs
        counter_sold_eggs += number_eggs

    command = input()

if command == "Close":
    print("Store is closed!")
    print(f"{counter_sold_eggs} eggs sold.")
