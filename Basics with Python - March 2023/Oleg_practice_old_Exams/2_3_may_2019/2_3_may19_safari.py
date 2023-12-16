budget = float(input())
need_lt_fuel = float(input())
day_of_week = input()

total_price = need_lt_fuel * 2.10 + 100

if day_of_week == "Saturday":
    total_price = (need_lt_fuel * 2.10 + 100) - (need_lt_fuel * 2.10 + 100) * 0.10

elif day_of_week == "Sunday":
    total_price = (need_lt_fuel * 2.10 + 100) - (need_lt_fuel * 2.10 + 100) * 0.20

if budget >= total_price:
    print(f"Safari time! Money left: {(budget - total_price):.2f} lv.")

else:
    print(f"Not enough money! Money needed: {(total_price - budget):.2f} lv.")
