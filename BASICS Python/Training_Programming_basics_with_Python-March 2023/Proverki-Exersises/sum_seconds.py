import math
from math import floor, ceil

time1 = int(input())
time2 = int(input())
time3 = int(input())
total_time = time1 + time2 + time3

minutes = total_time // 60
seconds = total_time % 60
minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')


