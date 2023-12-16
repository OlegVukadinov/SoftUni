km = int(input())
day_or_night = input()

price = 0.00
taxi_rate = 0.00

if day_or_night == 'day':
    taxi_rate = 0.79
else:
    taxi_rate = 0.90

if km < 20:
    price = 0.70 + km * taxi_rate

elif km < 100:
    price = km * 0.09

else:
    price = km * 0.06

print(f'{price:.2f}')


