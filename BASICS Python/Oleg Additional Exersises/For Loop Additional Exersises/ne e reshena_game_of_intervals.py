number_turns = int(input())

result = 0
counter_int_0_9 = 0
counter_int_10_19 = 0
counter_int_20_29 = 0
counter_int_30_39 = 0
counter_int_40_50 = 0
counter_invalid = 0
perc_number_int_0_9 = 0
perc_number_int_10_19 = 0
perc_number_int_20_29 = 0
perc_number_int_30_39 = 0
perc_number_int_40_50 = 0
perc_invalid = 0

for number in range(1, number_turns + 1):
    number_interval = int(input())

    if 0 <= number_interval < 10:
        result += number_interval * 0.20
        counter_int_0_9 += 1
        perc_number_int_0_9 = counter_int_0_9 / 10 * 100

    elif 10 <= number_interval < 20:
        result += number_interval * 0.30
        counter_int_10_19 += 1
        perc_number_int_10_19 = counter_int_10_19 / 10 * 100

    elif 20 <= number_interval < 30:
        result += number_interval * 0.40
        counter_int_20_29 += 1
        perc_number_int_20_29 = counter_int_20_29 / 10 * 100

    elif 30 <= number_interval < 40:
        result += 50
        counter_int_30_39 += 1
        perc_number_int_30_39 = counter_int_30_39 / 10 * 100

    elif 40 <= number_interval <= 50:
        result += 100
        counter_int_40_50 += 1
        perc_number_int_40_50 = counter_int_40_50 / 10 * 100

    elif 0 > number_interval or number_interval > 50:
        result = result / 2
        counter_invalid += 1
        perc_invalid = counter_invalid / 10 * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {perc_number_int_0_9:.2f}%")
print(f"From 10 to 19: {perc_number_int_10_19:.2f}%")
print(f"From 20 to 29: {perc_number_int_20_29:.2f}%")
print(f"From 30 to 39: {perc_number_int_30_39:.2f}%")
print(f"From 40 to 50: {perc_number_int_40_50:.2f}%")
print(f"Invalid numbers: {perc_invalid:.2f}%")




    #   20 / 100