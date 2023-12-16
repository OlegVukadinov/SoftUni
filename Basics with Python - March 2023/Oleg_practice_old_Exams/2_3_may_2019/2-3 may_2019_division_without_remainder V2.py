n = int(input())

counter_p1 = 0
counter_p2 = 0
counter_p3 = 0

for i in range (1, n + 1):
    cur_num = int(input())
    #counter_n += 1
    if cur_num % 2 == 0:
        counter_p1 += 1
    if cur_num % 3 == 0:
        counter_p2 += 1
    if cur_num % 4 == 0:
        counter_p3 += 1

perc_p1 = counter_p1/n * 100
perc_p2 = counter_p2/n * 100
perc_p3 = counter_p3/n * 100

print(f"{perc_p1:.2f}%")
print(f"{perc_p2:.2f}%")
print(f"{perc_p3:.2f}%")
