budget = float(input())
num_series = int(input())

price_counter = 0


for i in range(1, num_series + 1):
    name_series = input()
    price_series = float(input())


    if name_series == "Thrones":
        price_counter += price_series - price_series * 0.50

    elif name_series == "Lucifer":
        price_counter += price_series - price_series * 0.40

    elif name_series == "Protector":
        price_counter += price_series - price_series * 0.30

    elif name_series == "TotalDrama":
        price_counter += price_series - price_series * 0.20

    elif name_series == "Area":
        price_counter += price_series - price_series * 0.10

    else:
        price_counter += price_series

if budget >= price_counter:
    print(f"You bought all the series and left with {(budget - price_counter):.2f} lv.")
else:
    print(f"You need {(price_counter - budget):.2f} lv. more to buy the series!")