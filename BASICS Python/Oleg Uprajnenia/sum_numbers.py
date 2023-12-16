number = int(input())

counter_num = 0

while True:
    num = int(input())

    counter_num += num

    if counter_num >= number:
        print(f'{counter_num}')
        break