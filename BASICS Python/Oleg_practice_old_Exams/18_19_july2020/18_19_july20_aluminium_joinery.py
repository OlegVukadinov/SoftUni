number_joinery = int(input())
kind_joinery = input()
delivery = input()

single_price = 0

if kind_joinery == "90X130":
    single_price = 110
    if 30 <= number_joinery <= 60 :
        single_price = single_price - single_price * 0.05
    elif number_joinery > 60:
        single_price = single_price - single_price * 0.08
elif kind_joinery == "100X150":
    single_price = 140
    if 40 <= number_joinery <= 80 :
        single_price = single_price - single_price * 0.06
    elif number_joinery > 80:
        single_price = single_price - single_price * 0.10
elif kind_joinery == "130X180":
    single_price = 190
    if 20 <= number_joinery <= 50 :
        single_price = single_price - single_price * 0.07
    elif number_joinery > 50:
        single_price = single_price - single_price * 0.12
elif kind_joinery == "200X300":
    single_price = 250
    if 25 <= number_joinery <= 50:
        single_price = single_price - single_price * 0.09
    elif number_joinery > 50:
        single_price = single_price - single_price * 0.14

total_price = number_joinery * single_price

if delivery == "With delivery":
    total_price += 60
elif delivery == "Without delivery":
    total_price = total_price

if number_joinery > 99:
    total_price = total_price - total_price * 0.04

if number_joinery < 10:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")



