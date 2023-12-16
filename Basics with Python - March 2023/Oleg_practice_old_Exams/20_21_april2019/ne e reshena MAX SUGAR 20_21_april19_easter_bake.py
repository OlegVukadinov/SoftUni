from math import ceil

number_bakes = int(input())

counter_used_sugar_gr = 0
counter_used_flour_gr = 0
max_sugar = 0
max_flour = 0

for i in range(1, number_bakes + 1):
    used_sugar_gr = int(input())
    used_flour_gr = int(input())

    counter_used_sugar_gr += used_sugar_gr
    counter_used_flour_gr += used_flour_gr

    if max_sugar < used_sugar_gr:  # counter_used_sugar_gr:
        max_sugar = used_sugar_gr

    if max_flour < used_sugar_gr:  # counter_used_flour_gr:
        max_flour = used_flour_gr

print(f"Sugar: {ceil(counter_used_sugar_gr / 950)}")
print(f"Flour: {ceil(counter_used_flour_gr / 750)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")

# 57/100
