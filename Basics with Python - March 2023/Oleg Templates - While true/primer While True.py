while True:
    command = input()

    if command == "Stop":
        print("finish")
        break

    number = int(command)

    if number % 2 == 0:
        print(f"{number} is even")

    else:
        print(f"{number} is odd")

