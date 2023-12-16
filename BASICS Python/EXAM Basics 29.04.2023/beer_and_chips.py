from math import ceil

name_foot_fen = input()
budget = float(input())
number_beers = int(input())
number_chips = int(input())

total_beer_price = number_beers * 1.20
chips_price = total_beer_price * 0.45
total_chips_price = (ceil(chips_price * number_chips))

total_bill = total_beer_price + total_chips_price

if total_bill <= budget:
    print(f"{name_foot_fen} bought a snack and has {(budget - total_bill):.2f} leva left.")

else:
    print(f"{name_foot_fen} needs {(total_bill - budget):.2f} more leva!")
