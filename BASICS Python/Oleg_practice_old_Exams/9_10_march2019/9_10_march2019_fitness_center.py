number_visitors = int(input())

counter_back = 0
counter_chest = 0
counter_legs = 0
counter_abs = 0
counter_shake = 0
counter_bar = 0

for current_visitor in range (1, number_visitors + 1):
    workout = input()

    if workout == "Back":
        counter_back += 1
    elif workout == "Chest":
        counter_chest += 1
    elif workout == "Legs":
        counter_legs += 1
    elif workout == "Abs":
        counter_abs += 1
    elif workout == "Protein shake":
        counter_shake += 1
    elif workout == "Protein bar":
        counter_bar += 1

people_training = counter_back + counter_abs + counter_chest + counter_legs
people_protein = counter_shake + counter_bar
all_people = people_protein + people_training

print(f"{counter_back} - back")
print(f"{counter_chest} - chest")
print(f"{counter_legs} - legs")
print(f"{counter_abs} - abs")
print(f"{counter_shake} - protein shake")
print(f"{counter_bar} - protein bar")
print(f"{people_training / all_people * 100:.2f}% - work out")
print(f"{people_protein / all_people * 100:.2f}% - protein")