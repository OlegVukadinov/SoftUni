month = input()
number_nightstays = int(input())

price_studio = 0
price_apartment = 0

if month == 'May' or month == 'October':
    price_studio = 50
    price_apartment = 65
    if 7 < number_nightstays <= 14:
        price_studio = (price_studio - price_studio * 0.05)
    elif number_nightstays > 14:
        price_studio = (price_studio - price_studio * 0.3)

elif month == 'June' or month == 'September':
    price_studio = 75.20
    price_apartment = 68.70
    if number_nightstays > 14:
        price_studio = price_studio - price_studio * 0.2

elif month == 'July' or month == 'August':
    price_studio = 76
    price_apartment = 77

if number_nightstays > 14:
    price_apartment = price_apartment - (price_apartment * 0.1)

price_studio *= number_nightstays
price_apartment *= number_nightstays

print(f"Apartment: {price_apartment:.2f} lv.")

print(f"Studio: {price_studio:.2f} lv.")

