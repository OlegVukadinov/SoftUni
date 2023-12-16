nasledeni_money = float(input())
year_to_live = int(input())

counter_money = nasledeni_money
age_counter = 18

for i in range(1800, year_to_live + 1):
    # age_counter += 1
    if i % 2 == 0:
        counter_money -= 12000
    else:
        counter_money -= (12000 + 50 * age_counter)
    age_counter += 1

if counter_money >= 0:
    print(f"Yes! He will live a carefree life and will have {counter_money:.2f} dollars left.")

else:
    print(f"He will need {(abs(counter_money)):.2f} dollars to survive.")

