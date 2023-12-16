counter_kid = 0
counter_adult = 0
counter_toy = 0
counter_sweaters = 0

while True:
    command = input()

    if command == "Christmas":
        break
    years = int(command)

    if years <= 16:
        counter_kid += 1
        counter_toy += 1
    elif years > 16:
        counter_adult += 1
        counter_sweaters += 1

total_price_toys = counter_toy * 5
total_price_sweaters = counter_sweaters * 15

print(f"Number of adults: {counter_adult}")
print(f"Number of kids: {counter_kid}")
print(f"Money for toys: {total_price_toys}")
print(f"Money for sweaters: {total_price_sweaters}")
