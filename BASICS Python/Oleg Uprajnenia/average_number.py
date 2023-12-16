number = int(input())

counter = 0

for i in range(1, number + 1):
    n = int(input())

    counter += n

print(f"{counter / number:.2f}")