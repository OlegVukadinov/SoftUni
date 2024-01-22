number_locations = int(input())
counter_digged_gold_per_day = 0

for location in range(1, number_locations + 1):
    expected_average_dobiv_per_day = float(input())
    number_days_dig_location = int(input())
    for days in range(1,  number_days_dig_location + 1):
        digged_gold_per_day = float(input())
        counter_digged_gold_per_day += digged_gold_per_day
    average_dobiv_per_day = counter_digged_gold_per_day / number_days_dig_location

    if average_dobiv_per_day >= expected_average_dobiv_per_day:
        print(f"Good job! Average gold per day: {average_dobiv_per_day:.2f}.")
    elif average_dobiv_per_day < expected_average_dobiv_per_day:
        print(f"You need {(expected_average_dobiv_per_day - average_dobiv_per_day):.2f} gold.")
        break
    counter_digged_gold_per_day = 0