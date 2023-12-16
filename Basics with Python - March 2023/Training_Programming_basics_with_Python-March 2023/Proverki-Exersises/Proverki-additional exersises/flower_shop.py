from math import floor, ceil

num_magnolia = int(input())
num_zumbul = int(input())
num_roses = int(input())
num_cactus = int(input())
price_for_present = float(input())

order_flowers = num_magnolia * 3.25 + num_zumbul * 4 + num_roses * 3.50 + num_cactus * 8
pechalba = order_flowers - (order_flowers * 0.05)

if pechalba >= price_for_present:
    print(f'She is left with {floor(pechalba - price_for_present)} leva.')

else:
    print(f'She will have to borrow {ceil(price_for_present - pechalba)} leva.')

