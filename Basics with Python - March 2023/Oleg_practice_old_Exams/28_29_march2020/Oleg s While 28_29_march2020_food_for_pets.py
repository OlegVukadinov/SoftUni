days = int(input())
food = float(input())

counter_eaten_food = 0
counter_biscuits = 0
counter_eaten_food_dog = 0
counter_eaten_food_cat = 0

for current_day in range(1, days + 1):
    eaten_food_dog = int(input())
    eaten_food_cat = int(input())

    if current_day % 3 == 0:
        counter_biscuits += 0.10 * (eaten_food_dog + eaten_food_cat)

    counter_eaten_food_dog += eaten_food_dog
    counter_eaten_food_cat += eaten_food_cat
    counter_eaten_food += (eaten_food_dog + eaten_food_cat)

print(f"Total eaten biscuits: {round(counter_biscuits)}gr.")
print(f"{(counter_eaten_food / food * 100):.2f}% of the food has been eaten.")
print(f"{(counter_eaten_food_dog / counter_eaten_food * 100):.2f}% eaten from the dog.")
print(f"{(counter_eaten_food_cat / counter_eaten_food * 100):.2f}% eaten from the cat.")
