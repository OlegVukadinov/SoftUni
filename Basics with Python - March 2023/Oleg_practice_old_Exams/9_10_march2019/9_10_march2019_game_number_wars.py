first_player_name = input()
second_player_name = input()

counter_points_first_player = 0
counter_points_second_player = 0

# command = input()
while True:
    command = input()

    if command == "End of game":
        print(f"{first_player_name} has {counter_points_first_player} points")
        print(f"{second_player_name} has {counter_points_second_player} points")
        break

    first_card = int(command)
    second_card = int(input())

    if first_card > second_card:
        counter_points_first_player += first_card - second_card
    elif first_card < second_card:
        counter_points_second_player += second_card - first_card

    if first_card == second_card:
        print("Number wars!")
        command = input()
        first_card = int(command)
        second_card = int(input())

        if first_card > second_card:
            print(f"{first_player_name} is winner with {counter_points_first_player} points")
            break
        elif first_card < second_card:
            print(f"{second_player_name} is winner with {counter_points_second_player} points")
            break

