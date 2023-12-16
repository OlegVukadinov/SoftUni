days = int(input())
total_food = float(input())

total_food_eaten_by_dog = 0
total_food_eaten_by_cat = 0
total_eaten_food_per_day = 0
biscuits = 0

for i in range(1, days + 1):
    food_eaten_by_dog_per_day = int(input())
    total_food_eaten_by_dog += food_eaten_by_dog_per_day
    food_eaten_by_cat_per_day = int(input())
    total_food_eaten_by_cat += food_eaten_by_cat_per_day
    total_eaten_food_per_day += food_eaten_by_dog_per_day + food_eaten_by_cat_per_day
    if i % 3 == 0:
        biscuits += (food_eaten_by_cat_per_day + food_eaten_by_dog_per_day) * 0.10

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_eaten_food_per_day / total_food * 100:.2f}% of the food has been eaten.")
print(f"{total_food_eaten_by_dog / total_eaten_food_per_day * 100:.2f}% eaten from the dog.")
print(f"{total_food_eaten_by_cat / total_eaten_food_per_day * 100:.2f}% eaten from the cat.")
