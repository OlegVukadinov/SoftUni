x = float(input())
y = float(input())
h = float(input())

area_walls = (x * x - 1.2 * 2) + (x * x) + 2 * (x * y - 1.5 * 1.5)
area_roof = (x * y) * 2 + (x * h / 2) * 2

liters_green_paint = area_walls / 3.4
liters_red_paint = area_roof / 4.3

print(f"{liters_green_paint:.2f}")
print(f"{liters_red_paint:.2f}")