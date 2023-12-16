letter = None

stocks = int(input())
rooms = int(input())

for stock in range(stocks,0,-1):
    for room in range(0, rooms):
        if stock % 2 == 0:
            letter = "O"
        else:
            letter = "A"
        if stocks == stock:
            letter = "L"
        print(f'{letter}{stock}{room} ', end ="")
    print()