desired_profit_club = float(input())

counter_total_coctail_price = 0

while True:
    coctail_name = input()

    if coctail_name == "Party!":
        print(f"We need {desired_profit_club - counter_total_coctail_price:.2f} leva more.")
        break
    number_coctails = int(input())

    single_coctail_price = len(coctail_name)
    total_coctail_price = single_coctail_price * number_coctails

    if total_coctail_price % 2 == 1:
        total_coctail_price = total_coctail_price - total_coctail_price * 0.25

    counter_total_coctail_price += total_coctail_price

    if counter_total_coctail_price >= desired_profit_club:
        print(f"Target acquired.")
        break

print(f"Club income - {counter_total_coctail_price:.2f} leva.")