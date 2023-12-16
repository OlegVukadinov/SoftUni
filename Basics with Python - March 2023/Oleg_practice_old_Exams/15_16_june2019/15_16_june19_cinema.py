hall_capacity = int(input())
counter = 0
command = input()
money_income = 0
money = 0
total_people = 0
cinemaFull = 'False'

while command != "Movie time!":
    entering_people = int(command)
    if entering_people + total_people > hall_capacity:
        cinemaFull = 'True'
        break

    total_people += entering_people
    ticket_price = 5
    money_income = entering_people * ticket_price

    if entering_people % 3 == 0:
        money_income -= 5

    money += money_income

    command = input()

if cinemaFull == 'True':
    print("The cinema is full.")
    print(f"Cinema income - {money} lv.")

else:
    print(f"There are {hall_capacity - total_people} seats left in the cinema.")
    print(f"Cinema income - {money} lv.")