minutes_walking_per_day = int(input())
number_of_walking_per_day = int(input())
eated_calories_per_day = int(input())

total_walking_time = number_of_walking_per_day * minutes_walking_per_day
burned_calories = total_walking_time * 5

if burned_calories >= eated_calories_per_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")

else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")