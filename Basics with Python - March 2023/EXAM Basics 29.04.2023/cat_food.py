number_cats = int(input())

small_cats = 0
big_cats = 0
large_cats = 0
total_food = 0

for i in range(number_cats):
    food = float(input())

    total_food += food

    if 100 <= food < 200:

        small_cats += 1

    elif 200 <= food < 300:

        big_cats += 1

    elif 300 <= food < 400:

        large_cats += 1

food_price = total_food / 1000 * 12.45

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {large_cats} cats.")
print(f"Price for food per day: {food_price:.2f} lv.")