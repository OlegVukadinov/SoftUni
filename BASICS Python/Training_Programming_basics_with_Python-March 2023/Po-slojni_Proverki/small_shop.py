product = input()
town = input()
quantity = float(input())

price = 0

if town == 'Sofia':

   if product == 'coffee':
      price = quantity * 0.50

   elif product == 'water':
      price = quantity * 0.80

   elif product == 'beer':
      price = quantity * 1.20

   elif product == 'sweets':
      price = quantity * 1.45

   elif product == 'peanuts':
      price = quantity * 1.60

if town == "Plovdiv":
    if product == 'coffee':
        price = quantity * 0.40

    elif product == 'water':
        price = quantity * 0.70

    elif product == 'beer':
        price = quantity * 1.15

    elif product == 'sweets':
        price = quantity * 1.30

    elif product == 'peanuts':
        price = quantity * 1.50


if town == "Varna":
    if product == 'coffee':
        price = quantity * 0.45

    elif product == 'water':
        price = quantity * 0.70

    elif product == 'beer':
        price = quantity * 1.10

    elif product == 'sweets':
        price = quantity * 1.35

    elif product == 'peanuts':
        price = quantity * 1.55

print(price)
