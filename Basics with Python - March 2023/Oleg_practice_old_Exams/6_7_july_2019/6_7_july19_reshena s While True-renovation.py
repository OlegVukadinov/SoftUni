from math import ceil

h = int(input())
w = int(input())
perc_not_paint = int(input())

total_area_for_painting = h * w * 4
area_for_painting = ceil(total_area_for_painting - total_area_for_painting * perc_not_paint / 100)

while True:
    command = input()
    if command == "Tired!":
        print(f"{area_for_painting} quadratic m left.")
        break
    liters_paint = int(command)
    area_for_painting -= liters_paint


    if area_for_painting == 0:
        print("All walls are painted! Great job, Pesho!" )
        break

    if area_for_painting < 0:
        print(f"All walls are painted and you have {abs(area_for_painting)} l paint left!")
        break



