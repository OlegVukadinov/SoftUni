price_trip = float(input())
br_puzzles = int(input())
br_dolls = int(input())
br_bears = int(input())
br_minions = int(input())
br_trucks = int(input())

total_toys = br_puzzles + br_dolls + br_bears + br_minions + br_trucks


order = br_puzzles * 2.60 + br_dolls * 3 + br_bears * 4.10 + \
        br_minions * 8.20 + br_trucks * 2

if total_toys >= 50:
    order = order - (order * 0.25)

else:
    order = order

pechalba = order - (order * 0.1)

if pechalba >= price_trip:
    print(f'Yes! {pechalba - price_trip:.2f} lv left.')

else:
    print(f'Not enough money! {price_trip - pechalba:.2f} lv needed.')





