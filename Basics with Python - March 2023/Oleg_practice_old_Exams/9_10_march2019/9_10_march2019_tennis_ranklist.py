from math import floor

number_turn = int(input())
start_points = int(input())

counter_points = 0
counter_winner = 0

for current_turn in range (1, number_turn + 1):
    score = input()

    if score == "W":
        counter_points += 2000
        counter_winner += 1
    elif score == "F":
        counter_points += 1200
    if score == "SF":
        counter_points += 720

    total_points = counter_points + start_points

print(f"Final points: {total_points}")
print(f"Average points: {floor(counter_points / number_turn)}")
print(f"{(counter_winner / number_turn * 100):.2f}%")