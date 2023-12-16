type_proj = input()
rows = int(input())
columns = int(input())

profit = 0
places = rows * columns


if type_proj == 'Premiere':
    profit = places * 12.00

elif type_proj == 'Normal':
    profit = places * 7.50

elif type_proj == 'Discount':
    profit = places * 5.00

print(f'{profit:.2f} leva')