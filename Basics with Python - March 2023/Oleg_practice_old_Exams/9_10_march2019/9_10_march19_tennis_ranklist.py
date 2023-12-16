from math import floor
number_tournaments = int(input())
start_points = int(input())

counter_points = start_points
counter_tournaments = 0
counter_wins = 0

for i in range (1, number_tournaments + 1):
    level = input()
    counter_tournaments += 1

    if level == "W":
        counter_points += 2000
        counter_wins += 1

    elif level == "F":
        counter_points += 1200

    elif level == "SF":
        counter_points += 720

average_points = (counter_points - start_points) / number_tournaments
perc_winned_tournaments = counter_wins / number_tournaments * 100

print(f"Final points: {counter_points}")
print(f"Average points: {floor(average_points)}")
print(f"{perc_winned_tournaments:.2f}%")

