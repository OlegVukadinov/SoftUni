number_loads = int(input())

price_per_ton = 0
counter_microbus = 0
counter_truck = 0
counter_train = 0

for i in range(1, number_loads + 1):
    tons_load = int(input())

    if tons_load <= 3:  # микробус
        price_per_ton = 200
        counter_microbus += tons_load

    elif 4 <= tons_load <= 11:  # камион
        price_per_ton = 175
        counter_truck += tons_load

    elif tons_load >= 12:  # влак
        price_per_ton = 120
        counter_train += tons_load

total_tons = counter_microbus + counter_truck + counter_train

average_price_per_ton = (counter_microbus * 200 + counter_truck * 175 + counter_train * 120) / total_tons
perc_tons_microbus = counter_microbus / total_tons * 100
perc_tons_truck = counter_truck / total_tons * 100
perc_tons_train = counter_train / total_tons * 100

print(f'{average_price_per_ton:.2f}')
print(f'{perc_tons_microbus:.2f}%')
print(f'{perc_tons_truck:.2f}%')
print(f'{perc_tons_train:.2f}%')
