srok_dogovor = input()
type_dogovor = input()
added_internet = input()
number_mounts_pay = int(input())

price = 0
total_price = price * number_mounts_pay

if type_dogovor == "Small" and srok_dogovor == "one":
    price = 9.98
elif type_dogovor == "Small" and srok_dogovor == "two":
    price = 8.58
elif type_dogovor == "Middle" and srok_dogovor == "one":
    price = 18.99
elif type_dogovor == "Middle" and srok_dogovor == "two":
    price = 17.09
elif type_dogovor == "Large" and srok_dogovor == "one":
    price = 25.98
elif type_dogovor == "Large" and srok_dogovor == "two":
    price = 23.59
elif type_dogovor == "ExtraLarge" and srok_dogovor == "one":
    price = 35.99
elif type_dogovor == "ExtraLarge" and srok_dogovor == "two":
    price = 31.79

if added_internet == "yes" and price <= 10:
    price += 5.50
elif added_internet == "yes" and price <= 30:
    price += 4.35
elif added_internet == "yes" and price > 30:
    price += 3.85

total_price = price * number_mounts_pay

if srok_dogovor == "two":
    total_price = total_price - total_price * 0.0375

print(f"{total_price:.2f} lv.")
