volume_trunk = float(input())

counter_loaded_suitcases = 0
counter_volume_trunk = volume_trunk

command = input()

while command != "End":
    volume_suitcase = float(command)

    if (counter_loaded_suitcases + 1) % 3 == 0:
        volume_suitcase = volume_suitcase + volume_suitcase * 0.10

    if counter_volume_trunk < volume_suitcase:
        print("No more space!")
        break

    counter_volume_trunk -= volume_suitcase
    counter_loaded_suitcases += 1

    command = input()

if command == "End":
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {counter_loaded_suitcases} suitcases loaded.")
