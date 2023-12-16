name_1player = input()
name_2player = input()

point_counter_1player = 0
point_counter_2player = 0

command = input()

while command != "End of game":
    card_1player = int(command)
    card_2player = int(input())

    if card_1player > card_2player:
        point_counter_1player += (card_1player - card_2player)

    elif card_2player > card_1player:
        point_counter_2player += (card_2player - card_1player)

    elif card_2player == card_1player:
        print("Number wars!")
        card_1player = int(input())
        card_2player = int(input())

        if card_1player > card_2player:
            print(f"{name_1player} is winner with {point_counter_1player} points")
            break
        elif card_1player < card_2player:
            print(f"{name_2player} is winner with {point_counter_2player} points")
            break

    command = input()

if command == "End of game":
        print(f"{name_1player} has {point_counter_1player} points")
        print(f"{name_2player} has {point_counter_2player} points")