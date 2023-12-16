from math import ceil

name_serial = str(input())
time_epizod = int(input())
time_pochivka = int(input())

time_lunch = 1/8 * time_pochivka
time_relax = 1/4 * time_pochivka
need_time = time_pochivka - time_lunch - time_relax


if need_time >= time_epizod:
    print(f"You have enough time to watch {name_serial} and left with {ceil (need_time - time_epizod)} \
minutes free time.")

else:
    print(f"You don't have enough time to watch {name_serial}, you need {ceil (time_epizod- need_time)} \
more minutes.")