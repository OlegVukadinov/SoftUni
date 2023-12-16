number_groups = int(input())

counter_Musala = 0
counter_Monblan = 0
counter_Kilimanjaro = 0
counter_K2 = 0
counter_Everest = 0
counter_All = 0

for current_group in range(1, number_groups + 1):
    people_in_curr_group = int(input())

    if 1 <= people_in_curr_group <= 5:
        counter_Musala += people_in_curr_group
        counter_All += people_in_curr_group

    elif 6 <= people_in_curr_group <= 12:
        counter_Monblan += people_in_curr_group
        counter_All += people_in_curr_group

    elif 13 <= people_in_curr_group <= 25:
        counter_Kilimanjaro += people_in_curr_group
        counter_All += people_in_curr_group

    elif 26 <= people_in_curr_group <= 40:
        counter_K2 += people_in_curr_group
        counter_All += people_in_curr_group

    elif 41 <= people_in_curr_group:
        counter_Everest += people_in_curr_group
        counter_All += people_in_curr_group

print(f"{counter_Musala / counter_All * 100:.2f}%")
print(f"{counter_Monblan / counter_All * 100:.2f}%")
print(f"{counter_Kilimanjaro / counter_All * 100:.2f}%")
print(f"{counter_K2 / counter_All * 100:.2f}%")
print(f"{counter_Everest / counter_All * 100:.2f}%")
