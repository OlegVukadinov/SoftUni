command = input()
start_meters = 5364
peak_height = 8848
days_climbing = 1

while command != "END":
    meters_to_climb = int(input())

    if command == "Yes":
        days_climbing += 1
        if days_climbing > 5:
            print("Failed!")
            print(f"{start_meters}")
            break
        start_meters += meters_to_climb
    else:
        start_meters += meters_to_climb
    if start_meters >= peak_height:
        print(f"Goal reached for {days_climbing} days!")
        break

    command = input()

if command == "END":
    if start_meters >= peak_height:
        print(f"Goal reached for {days_climbing} days!")
    else:
        print("Failed!")
        print(f"{start_meters}")