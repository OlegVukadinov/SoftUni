number_celled_games = int(input())

# name_game = input()
counter_games = 0
counter_Hearthstone = 0
counter_Fornite = 0
counter_Overwatch = 0
counter_Others = 0

perc_Hearthstone = 0
perc_Fornite = 0
perc_Overwatch = 0
perc_Others = 0

for i in range(1, number_celled_games + 1):
    name_game = input()
    counter_games += 1

    if name_game == 'Hearthstone':
        counter_Hearthstone += 1
        perc_Hearthstone = counter_Hearthstone / number_celled_games * 100

    elif name_game == 'Fornite':
        counter_Fornite += 1
        perc_Fornite = counter_Fornite / number_celled_games * 100

    elif name_game == 'Overwatch':
        counter_Overwatch += 1
        perc_Overwatch = counter_Overwatch / number_celled_games * 100

    else:
        counter_Others += 1
        perc_Others = counter_Others / number_celled_games * 100

print(f"Hearthstone - {perc_Hearthstone:.2f}%")
print(f"Fornite - {perc_Fornite:.2f}%")
print(f"Overwatch - {perc_Overwatch:.2f}%")
print(f"Others - {perc_Others:.2f}%")
