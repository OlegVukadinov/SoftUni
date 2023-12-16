from math import ceil

price_1videocard = int(input())
price_1prehodn = int(input())
price_tok_videocard_per_day = float(input())
profit_from_videocard_per_day = float(input())

total_price_for_videocards = price_1videocard * 13
total_price_for_prehodn = price_1prehodn * 13
spent_money = total_price_for_videocards + total_price_for_prehodn + 1000

total_profit_videocard = (profit_from_videocard_per_day - price_tok_videocard_per_day) * 13

time_for_return_investition = spent_money / total_profit_videocard

print(f'{spent_money}')
print(f'{ceil(time_for_return_investition)}')