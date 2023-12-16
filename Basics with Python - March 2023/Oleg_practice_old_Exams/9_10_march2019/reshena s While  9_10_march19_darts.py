player_name = input()

counter_points = 301
successful_counter = 0
unsuccessful_counter = 0
area = input()

while area != "Retire":
    points = int(input())

    if area == "Single":
        points = points
    elif area == "Double":
        points = points * 2
    elif area == "Triple":
        points = points * 3

    if points <= counter_points:
        counter_points -= points
        successful_counter += 1

    elif points > counter_points:
        unsuccessful_counter += 1

    if counter_points == 0:
        print(f"{player_name} won the leg with {successful_counter} shots.")
        break

    area = input()

if area == "Retire":
    print(f"{player_name} retired after {unsuccessful_counter} unsuccessful shots.")



