num_numbers = int(input())
# numbers = int(input())

numbers_counter = 0
counter2 = 0
counter3 = 0
counter4 = 0
p1 = 0
p2 = 0
p3 = 0
for i in range(1, num_numbers + 1):
    numbers = int(input())
    numbers_counter += 1

    if numbers % 2 == 0:
        counter2 += 1
        p1 = counter2 / num_numbers * 100

    if numbers % 3 == 0:
        counter3 += 1
        p2 = counter3 / num_numbers * 100

    if numbers % 4 == 0:
        counter4 += 1
        p3 = counter4 / num_numbers * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')