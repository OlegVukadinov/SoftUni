from math import pi

figure = input()
area = 0

if figure == ('square'):
    side_a = float(input())
    area = side_a * side_a

elif figure == ('rectangle'):
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b

elif figure == ('circle'):
    r = float(input())
    area = pi * r * r

elif figure == ('triangle'):
    side_a = float(input())
    h = float(input())
    area = side_a * h / 2

print(f'{area:.3f}')










