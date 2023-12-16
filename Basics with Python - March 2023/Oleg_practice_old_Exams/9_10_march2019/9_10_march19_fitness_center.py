number_visitors = int(input())

counter_back = 0
counter_chest = 0
counter_legs = 0
counter_abs = 0
counter_protein = 0
trainers_counter = 0
counter_byers_shake = 0
counter_byers_bar = 0

for i in range(1, number_visitors + 1):
         visitor_action = input()

         if visitor_action == "Back":
             counter_back += 1
             trainers_counter += 1

         elif visitor_action == "Chest":
             counter_chest += 1
             trainers_counter += 1

         elif visitor_action == "Legs":
             counter_legs += 1
             trainers_counter += 1

         elif visitor_action == "Abs":
             counter_abs += 1
             trainers_counter += 1

         elif visitor_action == "Protein shake":
             counter_protein += 1
             counter_byers_shake += 1

         elif visitor_action == "Protein bar":
             counter_protein += 1
             counter_byers_bar += 1

all_byers_protein = counter_byers_shake + counter_byers_bar

perc_trainers = trainers_counter / number_visitors * 100
perc_byers_protein = all_byers_protein / number_visitors * 100

print(f"{counter_back} - back")
print(f"{counter_chest} - chest")
print(f"{counter_legs} - legs")
print(f"{counter_abs} - abs")
print(f"{counter_byers_shake} - protein shake")
print(f"{counter_byers_bar} - protein bar")
print(f"{perc_trainers:.2f}% - work out")
print(f"{perc_byers_protein:.2f}% - protein")
