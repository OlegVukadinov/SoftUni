from math import floor

number_balls = int(input())

total_points = 0
counter_red_balls = 0
counter_orange_balls = 0
counter_yellow_balls = 0
counter_white_balls = 0
counter_black_balls = 0
counter_other_balls = 0

for current_ball in range (1, number_balls + 1):
    colour = input()

    if colour == "red":
        total_points += 5
        counter_red_balls += 1
    elif colour == "orange":
        total_points += 10
        counter_orange_balls += 1
    elif colour == "yellow":
        total_points += 15
        counter_yellow_balls += 1
    elif colour == "white":
        total_points += 20
        counter_white_balls += 1
    elif colour == "black":
        total_points = floor(total_points / 2)
        counter_black_balls += 1
    elif colour != "black" or colour != "white" or colour != "yellow" or colour != "orange" or colour != "red":
        total_points += 0
        counter_other_balls += 1

print(f"Total points: {total_points}")
print(f"Red balls: {counter_red_balls}")
print(f"Orange balls: {counter_orange_balls}")
print(f"Yellow balls: {counter_yellow_balls}")
print(f"White balls: {counter_white_balls}")
print(f"Other colors picked: {counter_other_balls}")
print(f"Divides from black balls: {counter_black_balls}")