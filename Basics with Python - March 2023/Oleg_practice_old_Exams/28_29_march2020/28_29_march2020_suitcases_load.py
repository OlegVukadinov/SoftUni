volume = float(input())

counter_volume = 0
counter_suitcases = 0

while True:
    command = input()

    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break

    suitcase_volume = float(command)

    if (counter_suitcases + 1) % 3 == 0:
        suitcase_volume += suitcase_volume * 0.10

    counter_volume += suitcase_volume

    if counter_volume > volume:
        print("No more space!")
        break

    counter_suitcases += 1

print(f"Statistic: {counter_suitcases} suitcases loaded.")
