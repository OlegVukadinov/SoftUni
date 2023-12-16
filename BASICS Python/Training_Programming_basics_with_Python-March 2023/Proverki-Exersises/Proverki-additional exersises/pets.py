from math import ceil, floor

days = int(input())
food = int(input())
food_per_day_dog = float(input())
food_per_day_cat = float(input())
food_per_day_turtle = float(input())     # grams

needed_food = days * (food_per_day_dog + food_per_day_cat + food_per_day_turtle / 1000)

if food >= needed_food:
    print(f'{floor(food - needed_food)} kilos of food left.')

else:
    print(f'{ceil(needed_food - food)} more kilos of food are needed.')
