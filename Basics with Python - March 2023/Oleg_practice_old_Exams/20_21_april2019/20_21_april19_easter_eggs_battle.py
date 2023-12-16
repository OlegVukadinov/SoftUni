number_eggs_player1 = int(input())
number_eggs_player2 = int(input())

counter_eggs_player1 = number_eggs_player1
counter_eggs_player2 = number_eggs_player2

command = input()

while command != "End":

    if command == "one":
        counter_eggs_player2 -= 1

    elif command == "two":
        counter_eggs_player1 -= 1

    if counter_eggs_player1 == 0:
        print(f"Player one is out of eggs. Player two has {counter_eggs_player2} eggs left.")
        break

    elif counter_eggs_player2 == 0:
        print(f"Player two is out of eggs. Player one has {counter_eggs_player1} eggs left.")
        break

    command = input()

if command == "End":
    print(f"Player one has {counter_eggs_player1} eggs left.")
    print(f"Player two has {counter_eggs_player2} eggs left.")