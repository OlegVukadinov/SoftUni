our_money = float(input())
sex = input()
age = int(input())
sport = input()

price = 0

if sport == "Gym" and sex == 'm':
    price = 42
elif sport == "Gym" and sex == 'f':
    price = 35
elif sport == "Boxing" and sex == 'm':
    price = 41
elif sport == "Boxing" and sex == 'f':
    price = 37
elif sport == "Yoga" and sex == 'm':
    price = 45
elif sport == "Yoga" and sex == 'f':
    price = 42
elif sport == "Zumba" and sex == 'm':
    price = 34
elif sport == "Zumba" and sex == 'f':
    price = 31
elif sport == "Dances" and sex == 'm':
    price = 51
elif sport == "Dances" and sex == 'f':
    price = 53
elif sport == "Pilates" and sex == 'm':
    price = 39
elif sport == "Pilates" and sex == 'f':
    price = 37

if age <= 19:
    price -= price * 0.20

if our_money >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${(price - our_money):.2f} more.")