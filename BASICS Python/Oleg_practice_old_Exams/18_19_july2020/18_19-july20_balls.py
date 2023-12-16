from math import floor

number_of_balls = int(input())
points = 0
red_counter = 0
orange_counter = 0
yellow_counter = 0
white_counter = 0
black_counter = 0
other_color_counter = 0

for i in range(1, number_of_balls + 1):
    ball_color = input()

    if ball_color == 'red':
        points += 5
        red_counter += 1

    elif ball_color == 'orange':
        points += 10
        orange_counter += 1

    elif ball_color == 'yellow':
        points += 15
        yellow_counter += 1

    elif ball_color == 'white':
        points += 20
        white_counter += 1

    elif ball_color == 'black':
        points = floor(points / 2)
        black_counter += 1
    else:
        points = points
        other_color_counter += 1

print(f"Total points: {points:.0f}")
print(f"Red balls: {red_counter}")
print(f"Orange balls: {orange_counter}")
print(f"Yellow balls: {yellow_counter}")
print(f"White balls: {white_counter}")
print(f"Other colors picked: {other_color_counter}")
print(f"Divides from black balls: {black_counter}")

