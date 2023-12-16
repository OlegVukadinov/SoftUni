number_dancers = int(input())
points = float(input())
season = input()
place = input()

winned_sum = 0

if place == "Bulgaria":
    winned_sum = points * number_dancers
    if season == "summer":
        winned_sum = winned_sum - winned_sum * 0.05

    elif season == "winter":
        winned_sum = winned_sum - winned_sum * 0.08

elif place == "Abroad":
    winned_sum = (points * number_dancers) + (points * number_dancers) * 0.50

    if season == "summer":
        winned_sum = winned_sum - winned_sum * 0.10

    elif season == "winter":
        winned_sum = winned_sum - winned_sum * 0.15

blag_money = winned_sum * 0.75
total_sum = winned_sum - winned_sum * 0.75

money_for_dancers = total_sum / number_dancers

print(f"Charity - {blag_money:.2f}")
print(f"Money per dancer - {money_for_dancers:.2f}")
