number_locations = int(input())

gold_dug = 0
average_gold = 0
counter = 0
count_one = False
count_two = False

while number_locations > 0:
    expected_gold = float(input())
    mining_dig_days = int(input())

    while mining_dig_days > 0:
        gold_dug += float(input())
        mining_dig_days -= 1
        counter += 1

    if mining_dig_days == 0:
        average_gold = gold_dug / counter

        if average_gold >= expected_gold:
            print(f'Good job! Average gold per day: {average_gold:.2f}.')
            gold_dug -= gold_dug
            average_gold = 0
            counter = 0
            number_locations -= 1

        else:
            average_gold = expected_gold - average_gold
            print(f'You need {average_gold:.2f} gold.')
            gold_dug = 0
            counter = 0
            average_gold = 0

            number_locations -= 1