from math import floor

X = int(input())      # ground_sq_meters
Y = float(input())          # grape_ot_one_sq_meters
Z = int(input())        # needed_liters_wine
workers_num = int(input())

wine = X * Y * 0.40 / 2.5
diff = abs(wine - Z)

if wine < Z:
    print(f'It will be a tough winter! More {floor(diff)} liters wine needed.')

else:                                           # wine >= needed_liters_wine:
    print(f'Good harvest this year! Total wine: {floor(wine)} liters.')
    print(f'{floor(diff)} liters left -> {floor(diff / workers_num)} liters per person.')




