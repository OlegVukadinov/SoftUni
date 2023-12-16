from math import ceil

number_of_people = int(input())
tax_enter = float(input())
price_shezlong = float(input())
price_umbrella = float(input())

total_enter_price = number_of_people * tax_enter

all_money_for_shezlong = ceil(number_of_people * 0.75) * (price_shezlong)
# print(f"{all_money_for_shezlong: .2f}")
all_money_for_umbrella = ceil(0.50 * number_of_people) * (price_umbrella)
krayna_suma = total_enter_price + all_money_for_shezlong + all_money_for_umbrella

print(f'{krayna_suma:.2f} lv.')

# Raboti no ne zakruglq nagore
