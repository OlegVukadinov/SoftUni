price_strawberries = float(input())
kg_bananas = float(input())
kg_oranges = float(input())
kg_raspberries = float(input())
kg_strawberries = float(input())

price_raspberries = price_strawberries / 2
price_oranges = price_raspberries - price_raspberries * 0.40
price_bananas = price_raspberries - price_raspberries * 0.80

needed_money = price_strawberries * kg_strawberries + price_raspberries * kg_raspberries + price_oranges * \
        kg_oranges + price_bananas * kg_bananas

print(f'{needed_money:.2f}')
