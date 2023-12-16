number_bakes = int(input())
number_plates_eggs = int(input())
kg_kurabii = int(input())

price_bake = 3.20
price_plate_eggs = 4.35
price_kg_kurabii = 5.40
price_paint_for_eggs_per_plate = 0.15 * 12

total_price = price_bake * number_bakes + price_plate_eggs * number_plates_eggs\
              + price_kg_kurabii * kg_kurabii + price_paint_for_eggs_per_plate * number_plates_eggs

print(f'{total_price:.2f}')