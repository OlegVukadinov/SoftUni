budget = float(input())
num_nigts = int(input())
price_per_nights = float(input())
procent_add_razhodi = int(input())

if num_nigts > 7:
    price_per_nights = price_per_nights - price_per_nights * 0.05

total_price = num_nigts * price_per_nights + budget * procent_add_razhodi/100

if budget >= total_price:
    print(f'Ivanovi will be left with {(budget - total_price):.2f} leva after vacation.')

else:
    print(f'{(total_price - budget):.2f} leva needed.')