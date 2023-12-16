fruit = input()
package = input()
number_packages = int(input())

price = 0

if fruit == "Watermelon" and package == "small":
    price = 56 * 2
elif fruit == "Watermelon" and package == "big":
    price = 28.70 * 5

if fruit == "Mango" and package == "small":
    price = 36.66 * 2
elif fruit == "Mango" and package == "big":
    price = 19.60 * 5

if fruit == "Pineapple" and package == "small":
    price = 42.10 * 2
elif fruit == "Pineapple" and package == "big":
    price = 24.80 * 5

if fruit == "Raspberry" and package == "small":
    price = 20 * 2
elif fruit == "Raspberry" and package == "big":
    price = 15.20 * 5

total_price = price * number_packages

if 400 <= total_price <= 1000:
    total_price = total_price - total_price * 0.15
if total_price > 1000:
    total_price = total_price / 2

print(f"{total_price:.2f} lv.")