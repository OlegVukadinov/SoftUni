buyed_food_kg = int(input())

buyed_food_gr = buyed_food_kg * 1000

counter_eaten_food = 0

command = input()

while command != "Adopted":
    food_per_eat_gr = int(command)

    counter_eaten_food += food_per_eat_gr

    command = input()

    if command == "Adopted":
        if counter_eaten_food <= buyed_food_gr:
            print(f"Food is enough! Leftovers: {buyed_food_gr - counter_eaten_food} grams.")

        else:
            print(f"Food is not enough. You need {counter_eaten_food - buyed_food_gr} grams more.")


