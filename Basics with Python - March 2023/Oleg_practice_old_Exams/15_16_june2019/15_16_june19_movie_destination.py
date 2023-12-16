budget = float(input())
destination = input()
season = input()
number_of_days = int(input())

price_for_movie = 0

if destination == "Dubai" and season == "Winter":
    price_for_movie = 45000
elif destination == "Dubai" and season == "Summer":
    price_for_movie = 40000

if destination == "Sofia" and season == "Winter":
    price_for_movie = 17000
elif destination == "Sofia" and season == "Summer":
    price_for_movie = 12500

if destination == "London" and season == "Winter":
    price_for_movie = 24000
elif destination == "London" and season == "Summer":
    price_for_movie = 20250

total_price = number_of_days * price_for_movie

if destination == "Dubai":
    total_price = total_price - total_price * 0.30
elif destination == "Sofia":
    total_price = total_price + total_price * 0.25

diff = abs(total_price - budget)

if total_price <= budget:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")

elif total_price > budget:
    print(f"The director needs {diff:.2f} leva more!")