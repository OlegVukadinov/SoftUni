bottles_detergent = int(input())

detergent_ml = bottles_detergent * 750

counter_used_detergent = detergent_ml
counter_cicles = 0
counter_dishies = 0
counter_pots = 0

detergent_for_1dish = 5
detergent_for_1pot = 15

command = input()

while command != "End":
    number_vessels = int(command)

    counter_cicles += 1

    if counter_cicles % 3 == 0:
        counter_used_detergent -= number_vessels * 15
        counter_pots += number_vessels
    else:
        counter_used_detergent -= number_vessels * 5
        counter_dishies += number_vessels

    if counter_used_detergent < 0:
        print(f"Not enough detergent, {abs(counter_used_detergent)} ml. more necessary!")
        break

    command = input()

if command == "End":
    print("Detergent was enough!")
    print(f"{counter_dishies} dishes and {counter_pots} pots were washed.")
    print(f"Leftover detergent {counter_used_detergent} ml.")
