name = input()
number_matches = int(input())

counter_w = 0
counter_d = 0
counter_l = 0
counter_points = 0

for i in range(1, number_matches + 1):
    result = input()

    if result == 'W':
       counter_w += 1
       counter_points += 3

    elif result == 'D':
       counter_d += 1
       counter_points += 1

    elif result == 'L':
       counter_l += 1

if number_matches == 0:
    print(f"{name} hasn't played any games during this season.")

elif number_matches > 0:
    print(f"{name} has won {counter_points} points during this season.")
    print("Total stats:")
    print(f"## W: {counter_w}")
    print(f"## D: {counter_d}")
    print(f"## L: {counter_l}")
    print(f"Win rate: {(counter_w / number_matches * 100):.2f}%")
