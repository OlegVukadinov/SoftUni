n = int(input())

for a in range(1, 9):
    for b in range(9, a):
        for c in range(0, 9):
            for d in range(9, c):
    # summa = a + b + c + d
    # multiplication = a * b * c * d
                if (a + b + c + d) == (a * b * c * d) and n % 10 == 5:
                    print(f'{a}{b}{c}{d}')

                elif (a * b * c * d) % (a + b + c + d) == 3 and n % 3 == 0:
                    print(f'{d}{c}{b}{a}')

                else: # n != abcd or n != dcba :
                    print("Nothing found")
