import sys

max_num = -sys.maxsize
sum_numbers = 0

n = int(input())

for i in range(0, n):
    curr_num = int(input())
    sum_numbers += curr_num
    if curr_num > max_num:
        max_num = curr_num

sum_numbers -= max_num

if max_num == sum_numbers:
    print("Yes")
    print(f"Sum = {sum_numbers}")

else:
    print("No")
    sum_others = sum_numbers - max_num
    print(f'Diff = {abs(max_num - sum_numbers)}')




