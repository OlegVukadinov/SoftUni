hall_rent = float(input())

cake_price = hall_rent * 0.20
drinks = cake_price - cake_price * 0.45
animator = 1/3 * hall_rent

needed_budget = hall_rent + cake_price + drinks + animator

print(needed_budget)