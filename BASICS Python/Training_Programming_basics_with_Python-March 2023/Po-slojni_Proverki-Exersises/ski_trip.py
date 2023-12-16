days = int(input())
type_room = input()
rating = input()

price = 0
total_price = price * (days - 1)

if type_room == 'room for one person':
    price = 18
elif type_room == 'apartment':
    price = 25
    if days < 10:
        price = price - price * 0.30
    elif 10 <= days <= 15:
        price = price - price * 0.35
    elif days > 15:
        price = price - price * 0.50

elif type_room == 'president apartment':
    price = 35
    if days < 10:
        price = price - price * 0.10
    elif 10 <= days <= 15:
        price = price - price * 0.15
    elif days > 15:
        price = price - price * 0.20

if rating == 'positive':
    total_price = (price * (days - 1)) + (price * (days - 1) * 0.25)

elif rating == 'negative':
    total_price = (price * (days - 1)) - (price * (days - 1)) * 0.10

# total_price = price * (days - 1)

print(f'{total_price:.2f}')
