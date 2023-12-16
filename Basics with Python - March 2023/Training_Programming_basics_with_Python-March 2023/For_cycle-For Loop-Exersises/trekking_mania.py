number_of_groups = int(input())

all_people = 0
peak_musala = 0
peak_monblan = 0
peak_kilimanj = 0
peak_k2 = 0
peak_everest = 0

for i in range(1, number_of_groups + 1):
    number_of_people_in_group = int(input())
    all_people += number_of_people_in_group

    if number_of_people_in_group <= 5:
        peak_musala += number_of_people_in_group
    if 5 < number_of_people_in_group <= 12:
        peak_monblan += number_of_people_in_group
    if 12 < number_of_people_in_group <= 25:
        peak_kilimanj += number_of_people_in_group
    if 25 < number_of_people_in_group <= 40:
        peak_k2 += number_of_people_in_group
    if 40 < number_of_people_in_group :
        peak_everest += number_of_people_in_group

perc_musala = peak_musala / all_people * 100
print(f'{perc_musala:.2f}%')

perc_monblan = peak_monblan / all_people * 100
print(f'{perc_monblan:.2f}%')

perc_kilimanj = peak_kilimanj / all_people * 100
print(f'{perc_kilimanj:.2f}%')

perc_k2 = peak_k2 / all_people * 100
print(f'{perc_k2:.2f}%')

perc_everest = peak_everest / all_people * 100
print(f'{perc_everest:.2f}%')





