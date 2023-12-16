cur_hour = int(input())
cur_minutes = int(input())

time = cur_hour * 60 + cur_minutes + 15

hours = time // 60
minutes = time % 60

if hours > 23:
    hours = 0

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')



