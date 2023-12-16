numbers = int(input())

counter = 0

for i in range(1, numbers + 1):
    n = int(input())
    counter += n
print(f'{(counter / numbers):.2f}')