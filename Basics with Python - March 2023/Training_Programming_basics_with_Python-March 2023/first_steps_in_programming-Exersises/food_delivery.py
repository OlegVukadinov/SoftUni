broy_chicken_menu = int(input())
broy_fish_menu = int(input())
broy_veg_menu = int(input())

price_chicken_menu = broy_chicken_menu * 10.35
price_fish_menu = broy_fish_menu * 12.40
price_veg_menu = broy_veg_menu * 8.15

total_menu = price_chicken_menu + price_fish_menu + price_veg_menu
dessert = total_menu * 0.20
dostavka = 2.50

final_price = total_menu + dessert + dostavka
print(final_price)




