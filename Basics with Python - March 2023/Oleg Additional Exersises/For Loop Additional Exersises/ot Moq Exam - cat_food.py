number_cats = int(input())

counter_small_cats = 0
counter_big_cats = 0
counter_large_cats = 0
counter_price = 0

for i in range(1, number_cats + 1):
    x_gr_food = float(input())

    if 100 <= x_gr_food < 200:
        counter_small_cats += 1
        counter_price += x_gr_food

    elif 200 <= x_gr_food < 300:
        counter_big_cats += 1
        counter_price += x_gr_food

    elif 300 <= x_gr_food < 400:
        counter_large_cats += 1
        counter_price += x_gr_food

total_price_food = counter_price / 1000 * 12.45

print(f"Group 1: {counter_small_cats} cats.")
print(f"Group 2: {counter_big_cats} cats.")
print(f"Group 3: {counter_large_cats} cats.")
print(f"Price for food per day: {total_price_food:.2f} lv.")

