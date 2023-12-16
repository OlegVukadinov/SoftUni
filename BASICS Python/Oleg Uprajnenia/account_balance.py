counter = 0

while True:
    command = input()
    if command == "NoMoreMoney":
        break

    suma = float(command)
    if suma >= 0:
        counter += suma
        print(f'Increase: {suma}')

    elif suma < 0:
        print("Invalid operation!")
        break

print(f"Total: {counter:.2f}")
