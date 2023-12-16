budget = float(input())
broy_statisti = int(input())
price_clothes_per_statist = float(input())

decor_price = budget * 0.10
total_price_clothes = broy_statisti * price_clothes_per_statist
all_price = decor_price + total_price_clothes

if broy_statisti > 150:
    total_price_clothes = total_price_clothes - (total_price_clothes * 0.10)
# else:
   # total_price_clothes = total_price_clothes

if all_price > budget:
    print("Not enough money!")
    print(f'Wingard needs {abs(budget - all_price):.2f} leva more.')

else: # all_price <= budget
    print("Action!")
    print(f'Wingard starts filming with {abs(all_price - budget):.2f} leva left.')



