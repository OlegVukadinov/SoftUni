number_painted_eggs = int(input())

counter_red = 0
counter_orange = 0
counter_blue = 0
counter_green = 0
max_eggs = 0
max_eggs_color = ''

for i in range(1, number_painted_eggs + 1):
    color = input()

    if color == "red":
        counter_red += 1
        if max_eggs < counter_red:
            max_eggs = counter_red
            max_eggs_color = 'red'

    if color == "orange":
        counter_orange += 1
        if max_eggs < counter_orange:
            max_eggs = counter_orange
            max_eggs_color = 'orange'

    if color == "blue":
        counter_blue += 1
        if max_eggs < counter_blue:
            max_eggs = counter_blue
            max_eggs_color = 'blue'

    if color == "green":
        counter_green += 1
        if max_eggs < counter_green:
            max_eggs = counter_green
            max_eggs_color = 'green'

print(f"Red eggs: {counter_red}")
print(f"Orange eggs: {counter_orange}")
print(f"Blue eggs: {counter_blue}")
print(f"Green eggs: {counter_green}")
print(f"Max eggs: {max_eggs} -> {max_eggs_color}")


