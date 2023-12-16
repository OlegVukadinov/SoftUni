price_maiden_party = float(input())
number_love_message = int(input())
number_roses = int(input())
number_keyholder = int(input())
number_caricatures = int(input())
number_luck_suprise = int(input())

price_love_message = 0.60
price_roses = 7.20
price_keyholder = 3.60
price_caricatures = 18.20
price_luck_suprise = 22

total_articules_sum = price_love_message * number_love_message + price_roses * number_roses \
                      + price_keyholder * number_keyholder + price_caricatures * number_caricatures + price_luck_suprise * number_luck_suprise

number_all_articules = number_love_message + number_roses + number_keyholder + number_caricatures + number_luck_suprise

if number_all_articules >= 25:
    total_articules_sum = total_articules_sum - total_articules_sum * 0.35

profit = total_articules_sum - total_articules_sum * 0.10

if profit >= price_maiden_party:
    print(f"Yes! {profit - price_maiden_party:.2f} lv left.")

else:
    print(f"Not enough money! {(price_maiden_party - profit):.2f} lv needed.")
