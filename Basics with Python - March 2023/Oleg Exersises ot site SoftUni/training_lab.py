lenght_w = float(input()) * 100
width_h = float(input()) * 100

one_rab_place = 70 * 120
total_area = lenght_w * width_h

number_places_hall = ((total_area - one_rab_place - one_rab_place * 2) - (100 * (lenght_w - 80 - 120))) / one_rab_place
print(number_places_hall)